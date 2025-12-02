import re
import os
from docx import Document

# --- CONFIGURAÇÕES ---
ARQUIVO_MODELO = "leituras.docx"
ARQUIVO_SAIDA = "leituras_preenchidas.docx"

# --- BANCO DE DADOS ---
LIVROS_DB = {
    # HISTÓRICOS
    'gn': ('Gênesis', 'Históricos'), 'ex': ('Êxodo', 'Históricos'), 
    'lv': ('Levítico', 'Históricos'), 'nm': ('Números', 'Históricos'), 
    'dt': ('Deuteronômio', 'Históricos'), 'js': ('Josué', 'Históricos'), 
    'jz': ('Juízes', 'Históricos'), 'rt': ('Rute', 'Históricos'), 
    '1sm': ('1 Samuel', 'Históricos'), '2sm': ('2 Samuel', 'Históricos'), 
    '1rs': ('1 Reis', 'Históricos'), '2rs': ('2 Reis', 'Históricos'), 
    '1cr': ('1 Crônicas', 'Históricos'), '2cr': ('2 Crônicas', 'Históricos'), 
    'es': ('Esdras', 'Históricos'), 'ne': ('Neemias', 'Históricos'), 
    'tb': ('Tobias', 'Históricos'), 'jt': ('Judite', 'Históricos'), 
    'est': ('Ester', 'Históricos'), '1mc': ('1 Macabeus', 'Históricos'), 
    '2mc': ('2 Macabeus', 'Históricos'), 'at': ('Atos dos Apóstolos', 'Históricos'),
    # PROFETAS
    'jo': ('Jó', 'Profetas'), 'job': ('Jó', 'Profetas'),
    'sl': ('Salmos', 'Profetas'), 'pv': ('Provérbios', 'Profetas'), 
    'ecl': ('Eclesiastes', 'Profetas'), 'ct': ('Cântico dos Cânticos', 'Profetas'), 
    'sb': ('Sabedoria', 'Profetas'), 'eclo': ('Eclesiástico', 'Profetas'), 
    'is': ('Isaías', 'Profetas'), 'jr': ('Jeremias', 'Profetas'), 
    'lm': ('Lamentações', 'Profetas'), 'br': ('Baruc', 'Profetas'), 
    'ez': ('Ezequiel', 'Profetas'), 'dn': ('Daniel', 'Profetas'), 
    'os': ('Oseias', 'Profetas'), 'jl': ('Joel', 'Profetas'), 
    'am': ('Amós', 'Profetas'), 'ab': ('Abdias', 'Profetas'), 
    'jn': ('Jonas', 'Profetas'), 'mq': ('Miqueias', 'Profetas'), 
    'na': ('Naum', 'Profetas'), 'hc': ('Habacuc', 'Profetas'), 
    'sf': ('Sofonias', 'Profetas'), 'ag': ('Ageu', 'Profetas'), 
    'zc': ('Zacarias', 'Profetas'), 'ml': ('Malaquias', 'Profetas'),
    # EVANGELHO
    'mt': ('Mateus', 'Evangelho'), 'mc': ('Marcos', 'Evangelho'), 
    'lc': ('Lucas', 'Evangelho'), 'joao': ('João', 'Evangelho'), # Mudei a chave para evitar conflito com Jó, tratamos na função
    # CARTAS
    'rm': ('Romanos', 'Cartas'), '1cor': ('1 Coríntios', 'Cartas'), 
    '2cor': ('2 Coríntios', 'Cartas'), 'gl': ('Gálatas', 'Cartas'), 
    'ef': ('Efésios', 'Cartas'), 'fp': ('Filipenses', 'Cartas'), 
    'fl': ('Filipenses', 'Cartas'), 'cl': ('Colossenses', 'Cartas'), 
    '1ts': ('1 Tessalonicenses', 'Cartas'), '2ts': ('2 Tessalonicenses', 'Cartas'), 
    '1tm': ('1 Timóteo', 'Cartas'), '2tm': ('2 Timóteo', 'Cartas'), 
    'tt': ('Tito', 'Cartas'), 'fm': ('Filemom', 'Cartas'), 
    'hb': ('Hebreus', 'Cartas'), 'tg': ('Tiago', 'Cartas'), 
    '1pd': ('1 Pedro', 'Cartas'), '2pd': ('2 Pedro', 'Cartas'), 
    '1jo': ('1 João', 'Cartas'), '2jo': ('2 João', 'Cartas'), 
    '3jo': ('3 João', 'Cartas'), 'jd': ('Judas', 'Cartas'), 
    'ap': ('Apocalipse', 'Cartas')
}

def identificar_leitura(texto):
    texto_limpo = texto.strip()
    if not texto_limpo: return None, None

    match = re.match(r"^(\d?[A-Za-zÁ-ú]+)", texto_limpo)
    if match:
        abrev_original = match.group(1)
        abrev_lower = abrev_original.lower()
        
        nome_livro = ""
        categoria = "Desconhecido"

        # Tratamento específico para conflitos comuns
        if abrev_lower == 'jó':
             nome_livro, categoria = "Jó", "Profetas"
        elif abrev_lower == 'jo':
             nome_livro, categoria = "João", "Evangelho"
        elif abrev_lower in LIVROS_DB:
            nome_livro, categoria = LIVROS_DB[abrev_lower]
        
        if categoria != "Desconhecido":
            texto_formatado = texto_limpo.replace(abrev_original, nome_livro, 1)
            # Ajuste fino de formatação (espaço após nome)
            texto_formatado = re.sub(r"^"+nome_livro+r"\s*-\s*", f"{nome_livro} ", texto_formatado)
            return categoria, texto_formatado
    
    return "Desconhecido", texto_limpo

def preencher_word(dados_organizados):
    if not os.path.exists(ARQUIVO_MODELO):
        print(f"ERRO: O arquivo '{ARQUIVO_MODELO}' não foi encontrado.")
        return

    try:
        doc = Document(ARQUIVO_MODELO)
        print("Arquivo modelo carregado.")
        
        tabela_alvo = None
        indice_cabecalho = -1
        colunas_idx = {"Históricos": -1, "Profetas": -1, "Cartas": -1, "Evangelho": -1}

        encontrou = False
        print("Procurando tabela no documento...")
        
        for table in doc.tables:
            for i, row in enumerate(table.rows):
                texto_linha = [cell.text.strip() for cell in row.cells]
                
                if "Históricos" in texto_linha and "Profetas" in texto_linha:
                    tabela_alvo = table
                    indice_cabecalho = i
                    print(f"Tabela encontrada! Cabeçalhos na linha {i+1}.")
                    
                    for idx_cell, texto_cell in enumerate(texto_linha):
                        if texto_cell in colunas_idx:
                            colunas_idx[texto_cell] = idx_cell
                    
                    encontrou = True
                    break
            if encontrou: break
        
        if not tabela_alvo:
            print("\nERRO CRÍTICO: Não encontrei a tabela correta no Word.")
            return

        # Calcular linhas necessárias
        max_linhas = max(len(dados_organizados[cat]) for cat in colunas_idx.keys())
        linhas_totais = len(tabela_alvo.rows)
        linhas_dados_existentes = linhas_totais - (indice_cabecalho + 1)
        
        if linhas_dados_existentes < max_linhas:
            falta = max_linhas - linhas_dados_existentes
            print(f"Adicionando {falta} novas linhas na tabela...")
            for _ in range(falta):
                tabela_alvo.add_row()

        # Inserir dados
        for cat_nome, lista_leituras in dados_organizados.items():
            idx_coluna = colunas_idx[cat_nome]
            if idx_coluna == -1: continue 
            
            for i, leitura in enumerate(lista_leituras):
                linha_destino = indice_cabecalho + 1 + i
                cell = tabela_alvo.rows[linha_destino].cells[idx_coluna]
                cell.text = leitura

        doc.save(ARQUIVO_SAIDA)
        print(f"\nSUCESSO! Documento gerado: {ARQUIVO_SAIDA}")

    except Exception as e:
        print(f"Ocorreu um erro ao gerar o Word: {e}")