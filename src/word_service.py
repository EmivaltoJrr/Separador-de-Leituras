from functools import lru_cache
from io import BytesIO

from docx import Document

import banco_dados


class ErroGeracaoWord(Exception):
    """Falha ao gerar o documento (modelo ausente ou tabela não encontrada)."""


@lru_cache(maxsize=1)
def _bytes_modelo() -> bytes:
    # Lido do disco uma única vez; cada requisição abre uma cópia nova em memória.
    try:
        return banco_dados.ARQUIVO_MODELO.read_bytes()
    except FileNotFoundError:
        raise ErroGeracaoWord(f"O modelo '{banco_dados.ARQUIVO_MODELO.name}' não foi encontrado no servidor.")


def gerar_arquivo_word(dados_organizados: dict[str, list[str]]) -> bytes:
    """Preenche o modelo com as leituras e retorna os bytes do .docx gerado em memória (nada é salvo em disco)."""
    doc = Document(BytesIO(_bytes_modelo()))

    tabela_alvo = None
    indice_cabecalho = -1
    # Mapeamento dinâmico das colunas
    colunas_idx = {cat: -1 for cat in banco_dados.CATEGORIAS}

    # Lógica de busca da tabela
    for table in doc.tables:
        for i, row in enumerate(table.rows):
            texto_linha = [cell.text.strip() for cell in row.cells]

            # Identificador único da tabela
            if banco_dados.HISTORICOS in texto_linha and banco_dados.PROFETAS in texto_linha:
                tabela_alvo = table
                indice_cabecalho = i

                # Mapeia onde está cada coluna
                for idx_cell, texto_cell in enumerate(texto_linha):
                    if texto_cell in colunas_idx:
                        colunas_idx[texto_cell] = idx_cell
                break
        if tabela_alvo:
            break

    if not tabela_alvo:
        raise ErroGeracaoWord("Não encontrei no modelo a tabela com 'Históricos' e 'Profetas'.")

    # Expansão da tabela se necessário
    max_linhas = max((len(v) for v in dados_organizados.values()), default=0)
    linhas_dados_existentes = len(tabela_alvo.rows) - (indice_cabecalho + 1)
    for _ in range(max_linhas - linhas_dados_existentes):
        tabela_alvo.add_row()

    # Escrita dos dados
    for cat_nome, lista_leituras in dados_organizados.items():
        idx_coluna = colunas_idx.get(cat_nome, -1)
        if idx_coluna == -1:
            continue

        for i, leitura in enumerate(lista_leituras):
            linha_destino = indice_cabecalho + 1 + i
            tabela_alvo.rows[linha_destino].cells[idx_coluna].text = leitura

    buffer = BytesIO()
    doc.save(buffer)
    return buffer.getvalue()
