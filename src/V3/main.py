import os
import processamento
import word_service

def ler_arquivo_txt():
    print("\n--- ARQUIVOS DISPONÍVEIS ---")
    arquivos = [f for f in os.listdir('.') if f.lower().endswith('.txt') and os.path.isfile(f)]
    
    if not arquivos:
        print(">> Nenhum arquivo .txt encontrado.")
        return []

    for i, arquivo in enumerate(arquivos, 1):
        print(f"{i} - {arquivo}")
    
    while True:
        entrada = input("\nDigite o número do arquivo (ou 0 para voltar): ")
        if not entrada.isdigit(): continue
            
        escolha = int(entrada)
        if escolha == 0: return []
            
        if 1 <= escolha <= len(arquivos):
            nome_arquivo = arquivos[escolha - 1]
            break
        else:
            print("Número inválido.")

    try:
        print(f"\nLendo: '{nome_arquivo}'...")
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return [linha.strip() for linha in f.readlines() if linha.strip()]
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return []

def entrada_manual():
    leituras = []
    print("\nDigite as leituras (ex: 'Is 50,4'). Enter vazio para terminar.")
    while True:
        entrada = input(">> ")
        if not entrada.strip() or entrada.lower() == "sair": break
        leituras.append(entrada)
    return leituras

def main():
    print("\n" + "="*50)
    print(" ORGANIZADOR LITÚRGICO - MODULAR (V6)")
    print("="*50)
    
    # 1. Entrada de Dados
    print("1 - Escolher arquivo .txt")
    print("2 - Digitar manualmente")
    opcao = input("Opção: ").strip()
    
    if opcao == '1':
        leituras_raw = ler_arquivo_txt()
    elif opcao == '2':
        leituras_raw = entrada_manual()
    else:
        return

    if not leituras_raw:
        print("Sem dados para processar.")
        return

    # 2. Escolha de Formatação (NOVO)
    print("\n" + "-"*30)
    print("PREFERÊNCIA DE FORMATAÇÃO")
    print("-"*30)
    print("1 - Abreviado (ex: Gn 12,1)")
    print("2 - Completo  (ex: Gênesis 12,1)")
    fmt_escolha = input("Opção: ").strip()
    
    # Define a variável booleana baseada na escolha
    usar_abreviado = (fmt_escolha == '1')

    # 3. Processamento
    organizacao = {"Históricos": [], "Profetas": [], "Cartas": [], "Evangelho": []}
    fila = list(leituras_raw)
    
    print("\nProcessando...")
    while fila:
        item = fila.pop(0)
        
        # --- AQUI PASSAMOS A ESCOLHA DO USUÁRIO ---
        cat, texto_fmt = processamento.identificar_leitura(item, modo_abreviado=usar_abreviado)

        if cat == "Desconhecido" or cat == "Erro":
            print(f"\n[!] DÚVIDA: '{item}'")
            corrigido = input("    Corrija (ou Enter para ignorar): ")
            if corrigido.strip(): fila.insert(0, corrigido)
        else:
            organizacao[cat].append(texto_fmt)

    # 4. Resumo na Tela
    print("\n" + "-"*30 + "\nRESUMO\n" + "-"*30)
    for k, v in organizacao.items():
        if v:
            print(f"[{k}]:")
            for l in v: print(f"  - {l}")

    # 5. Geração do Word
    if input("\nGerar Word? (s/n): ").lower() == 's':
        word_service.gerar_arquivo_word(organizacao)
    else:
        print("Finalizado.")

if __name__ == "__main__":
    main()