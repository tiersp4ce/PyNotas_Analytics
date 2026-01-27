from processador import ProcessadorNotas

def main():
    sistema = ProcessadorNotas()
    
    sistema.carregar_dados()
    
    if not sistema.catalogo:
        print("Nenhum dado encontrado. Encerrando.")
        return

    print("\n" + "="*40)
    print(f" BASE DE DADOS PRONTA! ({len(sistema.catalogo)} produtos indexados)")
    print(" Digite o nome (ou parte dele) para buscar.")
    print(" Digite 'sair' para encerrar.")
    print("="*40)

    while True:
        termo = input("\nBuscar por: ").strip()
        
        if termo.lower() == 'sair':
            break
            
        resultados = sistema.buscar(termo)
        
        if resultados:
            print(f"\n✅ Encontrado(s) {len(resultados)} registro(s):\n")
            for res in resultados:
                print(f"   📦 Produto: {res['produto']}")
                print(f"   🏢 Fornecedor: {res['fornecedor']}")
                print(f"   🔑 Chave: {res['chave']}")  # <--- LINHA NOVA
                print(f"   📄 Nota Fiscal: {res['nota']}")
                print(f"   📅 Data: {res['data']}")
                print("-" * 30)
        else:
            print("❌ Nenhum produto encontrado.")

if __name__ == "__main__":
    main()
