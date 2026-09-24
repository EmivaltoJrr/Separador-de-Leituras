from io import BytesIO

from flask import Flask, jsonify, render_template, request, send_file

import banco_dados
import processamento
import word_service

app = Flask(__name__)
app.json.sort_keys = False  # mantém a ordem das colunas: Históricos, Profetas, Cartas, Evangelho
app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024  # 1 MB é mais do que suficiente para texto


def _ler_requisicao():
    dados = request.get_json(silent=True) or {}
    texto = dados.get("texto", "")
    formato = dados.get("formato", processamento.FORMATO_COMPLETO)
    ignorar = bool(dados.get("ignorar_desconhecidas", False))
    if not isinstance(texto, str):
        texto = ""
    return texto, formato, ignorar


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api/processar")
def processar():
    """Classifica o texto e devolve o resumo (pré-visualização) + erros."""
    texto, formato, _ = _ler_requisicao()
    leituras, erros = processamento.classificar_texto(texto)
    return jsonify({
        "resumo": processamento.organizar(leituras, formato),
        "erros": erros,
        "total": len(leituras),
    })


@app.post("/api/gerar")
def gerar():
    """Gera o .docx em memória e devolve como download."""
    texto, formato, ignorar = _ler_requisicao()
    leituras, erros = processamento.classificar_texto(texto)

    if erros and not ignorar:
        return jsonify({"mensagem": "Existem siglas não reconhecidas.", "erros": erros}), 422
    if not leituras:
        return jsonify({"mensagem": "Nenhuma leitura válida foi informada.", "erros": []}), 400

    try:
        conteudo = word_service.gerar_arquivo_word(processamento.organizar(leituras, formato))
    except word_service.ErroGeracaoWord as e:
        return jsonify({"mensagem": str(e), "erros": []}), 500

    return send_file(
        BytesIO(conteudo),
        as_attachment=True,
        download_name=banco_dados.NOME_DOWNLOAD,
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )


@app.errorhandler(413)
def arquivo_grande(_):
    return jsonify({"mensagem": "Texto muito grande (limite de 1 MB).", "erros": []}), 413


if __name__ == "__main__":
    app.run(debug=True)
