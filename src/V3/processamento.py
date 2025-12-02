import re
import banco_dados 

def identificar_leitura(texto, modo_abreviado=False):
    """
    Identifica o livro e retorna (Categoria, Texto Formatado).
    Se modo_abreviado=True, mantém 'Gn 1,1'.
    Se modo_abreviado=False, expande para 'Gênesis 1,1'.
    """
    try:
        texto_limpo = texto.strip()
        if not texto_limpo: return None, None

        match = re.match(r"^(\d?[A-Za-zÁ-ú]+)", texto_limpo)
        if match:
            abrev_original = match.group(1)
            abrev_lower = abrev_original.lower()
            
            nome_livro = ""
            categoria = "Desconhecido"
            bd = banco_dados.LIVROS_DB

            # Tratamentos manuais e busca no banco
            if abrev_lower == 'jó':
                nome_livro, categoria = "Jó", "Profetas"
            elif abrev_lower == 'jo':
                nome_livro, categoria = "João", "Evangelho"
            elif abrev_lower in bd:
                nome_livro, categoria = bd[abrev_lower]
            
            if categoria != "Desconhecido":
                # --- NOVA LÓGICA DE DECISÃO ---
                if modo_abreviado:
                    # Se o usuário quer abreviado, retornamos o texto original limpo
                    # (Mantém "Gn 1,1" em vez de trocar por "Gênesis")
                    return categoria, texto_limpo
                else:
                    # Lógica de expansão (Completo)
                    texto_formatado = texto_limpo.replace(abrev_original, nome_livro, 1)
                    texto_formatado = re.sub(r"^"+nome_livro+r"\s*-\s*", f"{nome_livro} ", texto_formatado)
                    return categoria, texto_formatado
        
        return "Desconhecido", texto_limpo

    except Exception as e:
        print(f"Erro interno ao processar '{texto}': {e}")
        return "Erro", texto