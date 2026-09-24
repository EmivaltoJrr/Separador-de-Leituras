import re
from dataclasses import dataclass

import banco_dados

DESCONHECIDO = "Desconhecido"
FORMATO_ABREVIADO = "abreviado"
FORMATO_COMPLETO = "completo"

_REGEX_SIGLA = re.compile(r"^(\d?[A-Za-zÁ-ú]+)")


@dataclass
class Leitura:
    linha: int          # número da linha (1-based) no texto original
    categoria: str
    completo: str       # ex: "Gênesis 12,1"
    abreviado: str      # ex: "Gn 12,1" (texto original limpo)


def identificar_leitura(texto: str) -> tuple[str | None, str | None, str | None]:
    """
    Retorna: (Categoria, Texto_Completo, Texto_Abreviado)
    """
    texto_limpo = texto.strip()
    if not texto_limpo:
        return None, None, None

    match = _REGEX_SIGLA.match(texto_limpo)
    if match:
        abrev_original = match.group(1)
        encontrado = banco_dados.LIVROS_DB.get(abrev_original.lower())

        if encontrado:
            nome_livro, categoria = encontrado
            # Gera a versão Completa
            texto_completo = texto_limpo.replace(abrev_original, nome_livro, 1)
            texto_completo = re.sub(r"^" + re.escape(nome_livro) + r"\s*-\s*", f"{nome_livro} ", texto_completo)
            return categoria, texto_completo, texto_limpo

    return DESCONHECIDO, texto_limpo, texto_limpo


def classificar_texto(texto: str) -> tuple[list[Leitura], list[dict]]:
    """
    Processa um bloco de texto (uma leitura por linha).
    Retorna (leituras reconhecidas, erros). Cada erro é {"linha": n, "texto": "..."}.
    """
    leituras, erros = [], []
    for num, linha in enumerate(texto.splitlines(), 1):
        cat, t_full, t_abrev = identificar_leitura(linha)
        if cat is None:
            continue
        if cat == DESCONHECIDO:
            erros.append({"linha": num, "texto": t_abrev})
        else:
            leituras.append(Leitura(num, cat, t_full, t_abrev))
    return leituras, erros


def organizar(leituras: list[Leitura], formato: str = FORMATO_COMPLETO) -> dict[str, list[str]]:
    """Agrupa as leituras por categoria, no formato escolhido."""
    organizacao = {cat: [] for cat in banco_dados.CATEGORIAS}
    for leitura in leituras:
        texto = leitura.abreviado if formato == FORMATO_ABREVIADO else leitura.completo
        organizacao[leitura.categoria].append(texto)
    return organizacao
