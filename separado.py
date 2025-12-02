import re

def classificar_liturgia():
    # --- BANCO DE DADOS (Abreviações -> Nome e Categoria) ---
    livros_db = {
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
        'lc': ('Lucas', 'Evangelho'), 
        'jo': ('João', 'Evangelho'), # Tratamento especial no código para diferenciar de Jó

        # CARTAS (Incluindo Apocalipse)
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

    # --- ENTRADA DE DADOS ---
    print("\n" + "="*50)
    print(" ORGANIZADOR LITÚRGICO")
    print("="*50)
    print("Instruções: Digite a leitura (ex: 'Is - 50,4') e aperte ENTER.")
    print("Quando terminar, deixe em branco e aperte ENTER para ver o resultado.\n")

    lista_leituras = []
    while True:
        entrada = input(">> Digite a leitura: ")
        
        # Condição de saída: Texto vazio ou digitar "sair"
        if entrada.strip() == "" or entrada.lower().strip() == "sair":
            break
            
        lista_leituras.append(entrada)

    # --- PROCESSAMENTO ---
    organizacao = {
        "Históricos": [],
        "Profetas": [],
        "Cartas": [],
        "Evangelho": [],
        "Desconhecido": []
    }

    print("\nProcessando...\n")

    for leitura in lista_leituras:
        leitura_limpa = leitura.strip()
        if not leitura_limpa: continue

        # Regex para capturar a sigla inicial (letras e talvez número inicial)
        match = re.match(r"^(\d?[A-Za-zÁ-ú]+)", leitura_limpa)
        
        if match:
            abrev_original = match.group(1)
            abrev_lower = abrev_original.lower()
            
            nome_livro = ""
            categoria = ""

            # Lógica para diferenciar Jó (Profeta) de João (Evangelho)
            if abrev_lower == 'jó':
                 nome_livro = "Jó"
                 categoria = "Profetas"
            elif abrev_lower == 'jo':
                 nome_livro = "João"
                 categoria = "Evangelho"
            elif abrev_lower in livros_db:
                nome_livro, categoria = livros_db[abrev_lower]
            else:
                categoria = "Desconhecido"
            
            if categoria != "Desconhecido":
                # Substitui a sigla pelo nome completo para ficar bonito
                texto_formatado = leitura_limpa.replace(abrev_original, nome_livro, 1)
                
                # Remove hífens extras se ficarem feios (ex: "Isaías - 50" -> "Isaías 50")
                # Opcional, mas ajuda na estética.
                texto_formatado = re.sub(r"^"+nome_livro+r"\s*-\s*", f"{nome_livro} ", texto_formatado)
                
                organizacao[categoria].append(texto_formatado)
            else:
                organizacao["Desconhecido"].append(leitura_limpa)
        else:
            organizacao["Desconhecido"].append(leitura_limpa)

    # --- SAÍDA DE DADOS ---
    print("="*40)
    print("RESULTADO FINAL")
    print("="*40)

    categorias_ordem = ["Históricos", "Profetas", "Cartas", "Evangelho"]

    tem_dados = False
    for cat in categorias_ordem:
        if organizacao[cat]:
            tem_dados = True
            print(f"\n[{cat.upper()}]")
            for item in organizacao[cat]:
                print(f"  • {item}")

    # Exibe erros de digitação, se houver
    if organizacao["Desconhecido"]:
        tem_dados = True
        print(f"\n[NÃO RECONHECIDO - VERIFIQUE A DIGITAÇÃO]")
        for item in organizacao["Desconhecido"]:
            print(f"  • {item}")

    if not tem_dados:
        print("\nNenhuma leitura foi inserida.")
    print("\n" + "="*40)

# Executa o programa
if __name__ == "__main__":
    classificar_liturgia()