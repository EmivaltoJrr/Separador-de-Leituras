from pathlib import Path

# --- CONFIGURAÇÕES DE ARQUIVOS ---
# Caminho absoluto: funciona independente do diretório de onde o servidor é iniciado.
ARQUIVO_MODELO = Path(__file__).resolve().parent.parent / "leituras.docx"
NOME_DOWNLOAD = "leituras_preenchidas.docx"

# --- CATEGORIAS ---
# Os nomes são idênticos aos cabeçalhos da tabela no leituras.docx.
HISTORICOS = "Históricos"
PROFETAS = "Profetas"
CARTAS = "Cartas"
EVANGELHO = "Evangelho"
CATEGORIAS = (HISTORICOS, PROFETAS, CARTAS, EVANGELHO)

# --- MAPEAMENTO DA BÍBLIA CATÓLICA ---
# 'jo' é João (Evangelho). Jó usa 'jó' (com acento) ou 'job'.
LIVROS_DB = {
    # --- HISTÓRICOS ---
    'gn': ('Gênesis', HISTORICOS), 'ex': ('Êxodo', HISTORICOS),
    'lv': ('Levítico', HISTORICOS), 'nm': ('Números', HISTORICOS),
    'dt': ('Deuteronômio', HISTORICOS), 'js': ('Josué', HISTORICOS),
    'jz': ('Juízes', HISTORICOS), 'rt': ('Rute', HISTORICOS),
    '1sm': ('1 Samuel', HISTORICOS), '2sm': ('2 Samuel', HISTORICOS),
    '1rs': ('1 Reis', HISTORICOS), '2rs': ('2 Reis', HISTORICOS),
    '1cr': ('1 Crônicas', HISTORICOS), '2cr': ('2 Crônicas', HISTORICOS),
    'es': ('Esdras', HISTORICOS), 'ne': ('Neemias', HISTORICOS),
    'tb': ('Tobias', HISTORICOS), 'jt': ('Judite', HISTORICOS),
    'est': ('Ester', HISTORICOS), '1mc': ('1 Macabeus', HISTORICOS),
    '2mc': ('2 Macabeus', HISTORICOS), 'at': ('Atos dos Apóstolos', HISTORICOS),

    # --- PROFETAS ---
    'jó': ('Jó', PROFETAS), 'job': ('Jó', PROFETAS),
    'sl': ('Salmos', PROFETAS), 'pv': ('Provérbios', PROFETAS),
    'ecl': ('Eclesiastes', PROFETAS), 'ct': ('Cântico dos Cânticos', PROFETAS),
    'sb': ('Sabedoria', PROFETAS), 'eclo': ('Eclesiástico', PROFETAS),
    'sir': ('Eclesiástico', PROFETAS), 'is': ('Isaías', PROFETAS),
    'jr': ('Jeremias', PROFETAS), 'lm': ('Lamentações', PROFETAS),
    'br': ('Baruc', PROFETAS), 'ez': ('Ezequiel', PROFETAS),
    'dn': ('Daniel', PROFETAS), 'os': ('Oseias', PROFETAS),
    'jl': ('Joel', PROFETAS), 'am': ('Amós', PROFETAS),
    'ab': ('Abdias', PROFETAS), 'jn': ('Jonas', PROFETAS),
    'mq': ('Miqueias', PROFETAS), 'na': ('Naum', PROFETAS),
    'hc': ('Habacuc', PROFETAS), 'sf': ('Sofonias', PROFETAS),
    'ag': ('Ageu', PROFETAS), 'zc': ('Zacarias', PROFETAS),
    'ml': ('Malaquias', PROFETAS),

    # --- EVANGELHO ---
    'mt': ('Mateus', EVANGELHO), 'mc': ('Marcos', EVANGELHO),
    'lc': ('Lucas', EVANGELHO), 'jo': ('João', EVANGELHO),
    'joao': ('João', EVANGELHO), 'joão': ('João', EVANGELHO),

    # --- CARTAS ---
    'rm': ('Romanos', CARTAS), '1cor': ('1 Coríntios', CARTAS),
    '2cor': ('2 Coríntios', CARTAS), 'gl': ('Gálatas', CARTAS),
    'ef': ('Efésios', CARTAS), 'fp': ('Filipenses', CARTAS),
    'fl': ('Filipenses', CARTAS), 'cl': ('Colossenses', CARTAS),
    '1ts': ('1 Tessalonicenses', CARTAS), '2ts': ('2 Tessalonicenses', CARTAS),
    '1tm': ('1 Timóteo', CARTAS), '2tm': ('2 Timóteo', CARTAS),
    'tt': ('Tito', CARTAS), 'fm': ('Filemom', CARTAS),
    'hb': ('Hebreus', CARTAS), 'tg': ('Tiago', CARTAS),
    '1pd': ('1 Pedro', CARTAS), '2pd': ('2 Pedro', CARTAS),
    '1jo': ('1 João', CARTAS), '2jo': ('2 João', CARTAS),
    '3jo': ('3 João', CARTAS), 'jd': ('Judas', CARTAS),
    'ap': ('Apocalipse', CARTAS)
}
