# Separador de Leituras

Aplicação web que separa referências bíblicas litúrgicas em **Históricos, Profetas, Cartas e Evangelho** e gera um documento Word (`.docx`) a partir do modelo `leituras.docx`. Não usa banco de dados nem grava arquivos: o `.docx` é montado em memória e enviado direto como download.

## Rodar localmente

```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/main.py                # http://127.0.0.1:5000
```

Testes: `python -m unittest discover -s tests`

## Siglas

Uma leitura por linha, ex.: `Gn 12,1-4`, `1Cor 1,27`. `Jo` é **João**; para **Jó** use `Jó` ou `Job`.

## Deploy (Render)

1. Suba o repositório no GitHub.
2. No Render: **New → Blueprint** e selecione o repositório (usa o `render.yaml`).
   Ou **New → Web Service** com:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn --chdir src main:app --bind 0.0.0.0:$PORT --workers 2`

O `Procfile` também serve para Railway/Heroku.
