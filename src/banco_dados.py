# --- CONFIGURAÇÕES DE ARQUIVOS ---
ARQUIVO_MODELO = "leituras.docx"
ARQUIVO_SAIDA = "leituras_preenchidas.docx"

# --- MAPEAMENTO DA BÍBLIA ---
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
    'lc': ('Lucas', 'Evangelho'), 'joao': ('João', 'Evangelho'),
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