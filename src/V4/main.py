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
            nome = arquivos[escolha - 1]
            break

    try:
        print(f"\nLendo: '{nome}'...")
        with open(nome, 'r', encoding='utf-8') as f:
            return [linha.strip() for linha in f.readlines() if linha.strip()]
    except Exception as e:
        print(f"Erro: {e}")
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
    print(" ORGANIZADOR LITÚRGICO - MODULAR (V7)")
    print("="*50)
    
    # 1. Entrada
    print("1 - Escolher arquivo .txt")
    print("2 - Digitar manualmente")
    op = input("Opção: ").strip()
    
    if op == '1':   raw = ler_arquivo_txt()
    elif op == '2': raw = entrada_manual()
    else: return

    if not raw: return

    # 2. Processamento (Agora guardamos os dados brutos processados)
    dados_processados = [] # Lista de tuplas: (categoria, texto_completo, texto_abrev)
    fila = list(raw)
    
    print("\nProcessando e separando...")
    while fila:
        item = fila.pop(0)
        cat, t_full, t_abrev = processamento.identificar_leitura(item)

        if cat == "Desconhecido" or cat == "Erro":
            print(f"\n[!] DÚVIDA: '{item}'")
            corrigido = input("    Corrija (ou Enter para ignorar): ")
            if corrigido.strip(): fila.insert(0, corrigido)
        else:
            # Guardamos tudo na memória temporária
            dados_processados.append((cat, t_full, t_abrev))

    # 3. Resumo na Tela (Mostra sempre o Completo para ficar bonito)
    # Criamos um dict temporário só para exibição
    resumo_visual = {"Históricos": [], "Profetas": [], "Cartas": [], "Evangelho": []}
    for cat, t_full, _ in dados_processados:
        if cat in resumo_visual:
            resumo_visual[cat].append(t_full)

    print("\n" + "-"*30 + "\nRESUMO DA SEPARAÇÃO\n" + "-"*30)
    for k, v in resumo_visual.items():
        if v:
            print(f"[{k}]:")
            for l in v: print(f"  - {l}")
    print("-" * 30)

    # 4. Decisão e Geração do Word
    resp = input("\nDeseja gerar o documento Word? (s/n): ").lower()
    if resp == 's':
        print("\nComo você quer preencher o arquivo?")
        print("1 - Abreviado (ex: Gn 12,1)")
        print("2 - Completo  (ex: Gênesis 12,1)")
        tipo_fmt = input("Opção: ").strip()
        
        # Monta o dicionário final baseado na escolha
        organizacao_final = {"Históricos": [], "Profetas": [], "Cartas": [], "Evangelho": []}
        
        for cat, t_full, t_abrev in dados_processados:
            if cat in organizacao_final:
                if tipo_fmt == '1':
                    organizacao_final[cat].append(t_abrev)
                else:
                    organizacao_final[cat].append(t_full)
        
        word_service.gerar_arquivo_word(organizacao_final)
    else:
        print("Finalizado.")

if __name__ == "__main__":
    main()