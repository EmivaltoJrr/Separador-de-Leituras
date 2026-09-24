# --- CONFIGURAÇÕES DE ARQUIVOS ---
ARQUIVO_MODELO = "leituras.docx"
ARQUIVO_SAIDA = "leituras_preenchidas.docx"

# --- MAPEAMENTO DA BÍBLIA CATÓLICA (ESTRUTURA SOLICITADA) ---
LIVROS_DB = {
    # --- HISTÓRICOS ---
    'gn': ('Gênesis', 'HISTÓRICOS'), 'ex': ('Êxodo', 'HISTÓRICOS'), 
    'lv': ('Levítico', 'HISTÓRICOS'), 'nm': ('Números', 'HISTÓRICOS'), 
    'dt': ('Deuteronômio', 'HISTÓRICOS'), 'js': ('Josué', 'HISTÓRICOS'), 
    'jz': ('Juízes', 'HISTÓRICOS'), 'rt': ('Rute', 'HISTÓRICOS'), 
    '1sm': ('1 Samuel', 'HISTÓRICOS'), '2sm': ('2 Samuel', 'HISTÓRICOS'), 
    '1rs': ('1 Reis', 'HISTÓRICOS'), '2rs': ('2 Reis', 'HISTÓRICOS'), 
    '1cr': ('1 Crônicas', 'HISTÓRICOS'), '2cr': ('2 Crônicas', 'HISTÓRICOS'), 
    'es': ('Esdras', 'HISTÓRICOS'), 'ne': ('Neemias', 'HISTÓRICOS'), 
    'tb': ('Tobias', 'HISTÓRICOS'), 'jt': ('Judite', 'HISTÓRICOS'), 
    'est': ('Ester', 'HISTÓRICOS'), '1mc': ('1 Macabeus', 'HISTÓRICOS'), 
    '2mc': ('2 Macabeus', 'HISTÓRICOS'), 'at': ('Atos dos Apóstolos', 'HISTÓRICOS'),

    # --- PROFETAS 
    'jo': ('Jó', 'PROFETAS'), 'job': ('Jó', 'PROFETAS'),
    'sl': ('Salmos', 'PROFETAS'), 'pv': ('Provérbios', 'PROFETAS'), 
    'ecl': ('Eclesiastes', 'PROFETAS'), 'ct': ('Cântico dos Cânticos', 'PROFETAS'), 
    'sb': ('Sabedoria', 'PROFETAS'), 'eclo': ('Eclesiástico', 'PROFETAS'), 
    'sir': ('Eclesiástico', 'PROFETAS'), 'is': ('Isaías', 'PROFETAS'), 
    'jr': ('Jeremias', 'PROFETAS'), 'lm': ('Lamentações', 'PROFETAS'), 
    'br': ('Baruc', 'PROFETAS'), 'ez': ('Ezequiel', 'PROFETAS'), 
    'dn': ('Daniel', 'PROFETAS'), 'os': ('Oseias', 'PROFETAS'), 
    'jl': ('Joel', 'PROFETAS'), 'am': ('Amós', 'PROFETAS'), 
    'ab': ('Abdias', 'PROFETAS'), 'jn': ('Jonas', 'PROFETAS'), 
    'mq': ('Miqueias', 'PROFETAS'), 'na': ('Naum', 'PROFETAS'), 
    'hc': ('Habacuc', 'PROFETAS'), 'sf': ('Sofonias', 'PROFETAS'), 
    'ag': ('Ageu', 'PROFETAS'), 'zc': ('Zacarias', 'PROFETAS'), 
    'ml': ('Malaquias', 'PROFETAS'),

    # --- EVANGELHO ---
    'mt': ('Mateus', 'EVANGELHO'), 'mc': ('Marcos', 'EVANGELHO'), 
    'lc': ('Lucas', 'EVANGELHO'), 'joao': ('João', 'EVANGELHO'), 
    'jo': ('João', 'EVANGELHO'), 

    # --- CARTAS ---
    'rm': ('Romanos', 'CARTAS'), '1cor': ('1 Coríntios', 'CARTAS'), 
    '2cor': ('2 Coríntios', 'CARTAS'), 'gl': ('Gálatas', 'CARTAS'), 
    'ef': ('Efésios', 'CARTAS'), 'fp': ('Filipenses', 'CARTAS'), 
    'fl': ('Filipenses', 'CARTAS'), 'cl': ('Colossenses', 'CARTAS'), 
    '1ts': ('1 Tessalonicenses', 'CARTAS'), '2ts': ('2 Tessalonicenses', 'CARTAS'), 
    '1tm': ('1 Timóteo', 'CARTAS'), '2tm': ('2 Timóteo', 'CARTAS'), 
    'tt': ('Tito', 'CARTAS'), 'fm': ('Filemom', 'CARTAS'), 
    'hb': ('Hebreus', 'CARTAS'), 'tg': ('Tiago', 'CARTAS'), 
    '1pd': ('1 Pedro', 'CARTAS'), '2pd': ('2 Pedro', 'CARTAS'), 
    '1jo': ('1 João', 'CARTAS'), '2jo': ('2 João', 'CARTAS'), 
    '3jo': ('3 João', 'CARTAS'), 'jd': ('Judas', 'CARTAS'), 
    'ap': ('Apocalipse', 'CARTAS')
}