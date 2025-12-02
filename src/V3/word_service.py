import os
from docx import Document
import banco_dados # Para pegar os nomes dos arquivos

def gerar_arquivo_word(dados_organizados):
    arquivo_modelo = banco_dados.ARQUIVO_MODELO
    arquivo_saida = banco_dados.ARQUIVO_SAIDA

    if not os.path.exists(arquivo_modelo):
        print(f"ERRO DE ARQUIVO: O modelo '{arquivo_modelo}' não existe na pasta.")
        print("Certifique-se de que o arquivo leituras.docx está junto com o script.")
        return

    try:
        doc = Document(arquivo_modelo)
        print("Arquivo modelo carregado na memória.")
        
        tabela_alvo = None
        indice_cabecalho = -1
        # Mapeamento dinâmico das colunas
        colunas_idx = {"Históricos": -1, "Profetas": -1, "Cartas": -1, "Evangelho": -1}

        encontrou = False
        print("Procurando tabela no documento...")
        
        # Lógica de busca da tabela
        for table in doc.tables:
            for i, row in enumerate(table.rows):
                texto_linha = [cell.text.strip() for cell in row.cells]
                
                # Identificador único da sua tabela
                if "Históricos" in texto_linha and "Profetas" in texto_linha:
                    tabela_alvo = table
                    indice_cabecalho = i
                    print(f"Tabela localizada! Cabeçalhos na linha {i+1}.")
                    
                    # Mapeia onde está cada coluna
                    for idx_cell, texto_cell in enumerate(texto_linha):
                        if texto_cell in colunas_idx:
                            colunas_idx[texto_cell] = idx_cell
                    
                    encontrou = True
                    break
            if encontrou: break
        
        if not tabela_alvo:
            print("\nERRO CRÍTICO: Não encontrei a tabela com 'Históricos' e 'Profetas'.")
            return

        # Expansão da tabela se necessário
        max_linhas = 0
        for cat in colunas_idx.keys():
            if cat in dados_organizados:
                max_linhas = max(max_linhas, len(dados_organizados[cat]))

        linhas_totais = len(tabela_alvo.rows)
        linhas_dados_existentes = linhas_totais - (indice_cabecalho + 1)
        
        if linhas_dados_existentes < max_linhas:
            falta = max_linhas - linhas_dados_existentes
            print(f"Expandindo tabela: adicionando {falta} linhas...")
            for _ in range(falta):
                tabela_alvo.add_row()

        # Escrita dos dados
        for cat_nome, lista_leituras in dados_organizados.items():
            idx_coluna = colunas_idx.get(cat_nome, -1)
            if idx_coluna == -1: continue 
            
            for i, leitura in enumerate(lista_leituras):
                linha_destino = indice_cabecalho + 1 + i
                cell = tabela_alvo.rows[linha_destino].cells[idx_coluna]
                cell.text = leitura

        doc.save(arquivo_saida)
        print(f"\nSUCESSO TOTAL! Arquivo salvo como: {arquivo_saida}")

    except PermissionError:
        print(f"\nERRO DE PERMISSÃO: O arquivo '{arquivo_saida}' parece estar aberto.")
        print("Feche o Word e tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao gerar o Word: {e}")