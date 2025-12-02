import os
import funcoes

def ler_arquivo_txt():
    """Lista arquivos .txt da pasta e pede para o usuário escolher um número."""
    print("\n--- ARQUIVOS DISPONÍVEIS ---")
    
    # 1. Filtra apenas arquivos que terminam com .txt
    arquivos = [f for f in os.listdir('.') if f.lower().endswith('.txt') and os.path.isfile(f)]
    
    if not arquivos:
        print(">> Nenhum arquivo .txt encontrado nesta pasta.")
        return []

    # 2. Mostra a lista numerada
    for i, arquivo in enumerate(arquivos, 1):
        print(f"{i} - {arquivo}")
    
    # 3. Loop de validação da escolha
    while True:
        entrada = input("\nDigite o número do arquivo (ou 0 para voltar): ")
        
        # Se o usuário digitar algo que não é número, avisamos
        if not entrada.isdigit():
            print("Por favor, digite apenas números.")
            continue
            
        escolha = int(entrada)
        
        if escolha == 0:
            return [] # Usuário desistiu
            
        if 1 <= escolha <= len(arquivos):
            nome_arquivo = arquivos[escolha - 1] # Pega o nome correto na lista
            break
        else:
            print("Número inválido. Escolha uma das opções da lista.")

    # 4. Lê o arquivo escolhido
    try:
        print(f"\nLendo arquivo: '{nome_arquivo}'...")
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            linhas = [linha.strip() for linha in f.readlines() if linha.strip()]
        print(f"{len(linhas)} leituras carregadas com sucesso!")
        return linhas
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return []

def entrada_manual():
    """Captura input do usuário linha a linha."""
    leituras = []
    print("\nDigite as leituras (ex: 'Is 50,4'). Enter vazio para terminar.")
    while True:
        entrada = input(">> ")
        if entrada.strip() == "" or entrada.lower() == "sair":
            break
        leituras.append(entrada)
    return leituras

def main():
    print("\n" + "="*50)
    print(" ORGANIZADOR LITÚRGICO & WORD (V4)")
    print("="*50)
    
    # --- 1. SELEÇÃO DE MODO ---
    print("Como você deseja inserir as leituras?")
    print("1 - Escolher um arquivo da pasta")
    print("2 - Digitar manualmente")
    
    opcao = input("Opção: ").strip()
    leituras_raw = []

    if opcao == '1':
        leituras_raw = ler_arquivo_txt()
    elif opcao == '2':
        leituras_raw = entrada_manual()
    else:
        print("Opção inválida. Encerrando.")
        return

    # Se a lista estiver vazia (erro na leitura ou usuário cancelou)
    if not leituras_raw:
        print("Nenhuma leitura para processar. Encerrando.")
        return

    # --- 2. PROCESSAMENTO E SEPARAÇÃO ---
    organizacao = {"Históricos": [], "Profetas": [], "Cartas": [], "Evangelho": []}
    fila_processamento = list(leituras_raw)
    
    print("\nProcessando leituras...")
    
    while fila_processamento:
        item = fila_processamento.pop(0)
        cat, texto_fmt = funcoes.identificar_leitura(item)

        if cat == "Desconhecido":
            print(f"\n[!] NÃO RECONHECIDO: '{item}'")
            corrigido = input("    Digite a correção (ou Enter para ignorar): ")
            if corrigido.strip():
                fila_processamento.insert(0, corrigido)
        else:
            organizacao[cat].append(texto_fmt)

    # --- 3. EXIBIR RESUMO (SEPARAÇÃO) ---
    print("\n" + "-"*40)
    print("RESUMO FINAL DA SEPARAÇÃO")
    print("-" + "-"*39)
    for k, v in organizacao.items():
        if v:
            print(f"[{k.upper()}]:")
            for l in v: print(f"  - {l}")
        else:
            print(f"[{k.upper()}]: (vazio)")
    print("-" + "-"*39)

    # --- 4. GERAR WORD ---
    resp = input("\nDeseja gerar o documento Word com esses dados? (s/n): ")
    if resp.lower() == 's':
        funcoes.preencher_word(organizacao)
    else:
        print("Operação finalizada sem gerar arquivo.")

if __name__ == "__main__":
    main()