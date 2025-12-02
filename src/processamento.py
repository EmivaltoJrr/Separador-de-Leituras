import re
import banco_dados 

def identificar_leitura(texto):
    """
    Retorna: (Categoria, Texto_Completo, Texto_Abreviado)
    """
    try:
        texto_limpo = texto.strip()
        if not texto_limpo: return None, None, None

        match = re.match(r"^(\d?[A-Za-zÁ-ú]+)", texto_limpo)
        if match:
            abrev_original = match.group(1)
            abrev_lower = abrev_original.lower()
            
            nome_livro = ""
            categoria = "Desconhecido"
            bd = banco_dados.LIVROS_DB

            if abrev_lower == 'jó':
                nome_livro, categoria = "Jó", "Profetas"
            elif abrev_lower == 'jo':
                nome_livro, categoria = "João", "Evangelho"
            elif abrev_lower in bd:
                nome_livro, categoria = bd[abrev_lower]
            
            if categoria != "Desconhecido":
                # Gera a versão Completa
                texto_completo = texto_limpo.replace(abrev_original, nome_livro, 1)
                texto_completo = re.sub(r"^"+nome_livro+r"\s*-\s*", f"{nome_livro} ", texto_completo)
                
                # Retorna: Categoria, Versão Completa, Versão Abreviada (original limpa)
                return categoria, texto_completo, texto_limpo
        
        return "Desconhecido", texto_limpo, texto_limpo

    except Exception as e:
        print(f"Erro interno ao processar '{texto}': {e}")
        return "Erro", texto, texto