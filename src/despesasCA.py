import pandas as pd # type: ignore
import os
#By: Herick Marlon

# Função para exibir o menu
def exibir_menu():
    print("\nGerenciador de Despesas\n")
    print("1. Adicionar uma despesa \n")
    print("2. Editar uma despesa \n")
    print("3. Exibir todas as despesas \n")
    print("4. Salvar despesas em Excel \n")
    print("5. Sair \n")

# Função para exibir despesas
def exibir_despesas(despesas):
    if despesas.empty:
        print("\nNenhuma despesa cadastrada.")
    else:
        print("\nDespesas cadastradas:")
        print(despesas)

# Função para adicionar uma despesa
def adicionar_despesa(despesas):
    descricao = input("Descrição da despesa: ")
    valor = float(input("Valor da despesa: "))
    categoria = input("Categoria da despesa: ")
    data = input("Data da despesa (dd/mm/aaaa): ")
    
    nova_despesa = pd.DataFrame({
        "Descrição": [descricao],
        "Valor": [valor],
        "Categoria": [categoria],
        "Data": [data]
    })
    return pd.concat([despesas, nova_despesa], ignore_index=True)

# Função para editar uma despesa
def editar_despesa(despesas):
    if despesas.empty:
        print("\nNenhuma despesa para editar.")
        return despesas

    exibir_despesas(despesas)
    try:
        indice = int(input("Digite o número da despesa que deseja editar (índice): "))
        if indice < 0 or indice >= len(despesas):
            print("Índice inválido!")
            return despesas

        print("\nEditando despesa:")
        print(despesas.iloc[indice])
        despesas.loc[indice, "Descrição"] = input("Nova descrição (ou pressione Enter para manter): ") or despesas.loc[indice, "Descrição"]
        despesas.loc[indice, "Valor"] = float(input("Novo valor (ou pressione Enter para manter): ") or despesas.loc[indice, "Valor"])
        despesas.loc[indice, "Categoria"] = input("Nova categoria (ou pressione Enter para manter): ") or despesas.loc[indice, "Categoria"]
        despesas.loc[indice, "Data"] = input("Nova data (ou pressione Enter para manter): ") or despesas.loc[indice, "Data"]
    except ValueError:
        print("Entrada inválida!")
    return despesas

# Função para salvar despesas em Excel
def salvar_em_excel(despesas):
    caminho = "generated/"
    nome_arquivo = input("Digite o nome do arquivo Excel (exemplo: despesas.xlsx): ")
    if not nome_arquivo.endswith(".xlsx"):
        nome_arquivo += ".xlsx"
    despesas.to_excel(caminho + nome_arquivo, index=False, engine="openpyxl")
    print(f"Despesas salvas no arquivo '{nome_arquivo}'.")

# Função principal
def main():
    despesas = pd.DataFrame(columns=["Descrição", "Valor", "Categoria", "Data"])
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            despesas = adicionar_despesa(despesas)
        elif opcao == "2":
            despesas = editar_despesa(despesas)
        elif opcao == "3":
            exibir_despesas(despesas)
        elif opcao == "4":
            salvar_em_excel(despesas)
        elif opcao == "5":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
