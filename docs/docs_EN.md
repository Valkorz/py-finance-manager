# PY-FINANCE-MANAGER
#### A python finance manager using pandas and openpyxl, which allows the user to manage their expenses through an interface, which is then tracked by an excel sheet.

---
### Functionalities:

- Displaying existing expenses;
- Adding new expenses;
- Editing existing expenses;
- Export dataframe as Excel file;

---

## Displaying expenses

```py
def exibir_despesas(despesas):
    if despesas.empty:
        print("\nNenhuma despesa cadastrada.")
    else:
        print("\nDespesas cadastradas:")
        print(despesas)
```

Expenses are displayed as "DataFrames", this example showcases the implementation of the `exibir_despesas` function where the full pandas dataframe of expenses is printed out in the console.

---

## Adding new expenses

```py
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
```

An expense is a class that contains a description, value, category and date. This expense is filled out and then inserted into the expenses dataframe. This action is done by prompting the user into input of data, which is then transformed into a dataframe and concatenated into the main dataframe (so that all expenses are stored in the same variable, as an array). The following snippet contains the implementation of the expenses (`despesas`) class.

```py
class despesa:
    valor = 0.0
    nome = ""
    data = ""
    descricao = ""

    def __init__(self, nome : str, valor : float, data : str, descricao : str):
        self.valor = valor
        self.nome = nome
        self.data = data
        self.descricao = descricao
```
---
## Editing existing expenses

```py
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

```

The snippet above describes the action of editing an existing entry in the dataFrame (if it exists). The function prints out the whole dataframe, and the user must select the specific entry they wish to modify, which is done by an input prompt by index. The specified index will be located in the dataframe list and modified by user input.

---

## Exporting dataFrame as Excel file

```py
def salvar_em_excel(despesas):
    caminho = "generated/"
    nome_arquivo = input("Digite o nome do arquivo Excel (exemplo: despesas.xlsx): ")
    if not nome_arquivo.endswith(".xlsx"):
        nome_arquivo += ".xlsx"
    despesas.to_excel(caminho + nome_arquivo, index=False, engine="openpyxl")
    print(f"Despesas salvas no arquivo '{nome_arquivo}'.")
```

This snippet is responsible for collecting the expenses dataFrame and then creating an Excel sheet inside the `generated` folder. It prompts the user to input a name for the file, and adds the correct file extension (if missing). It creates the sheet by using the `openpyxl` library.