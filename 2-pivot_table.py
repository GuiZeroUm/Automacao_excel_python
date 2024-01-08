import pandas as pd

# 1- Importando dados
data = pd.read_excel("./data/VendaCarros.xlsx")
print (data)

# 2- Selecionando colunas especificas
df = data[["Fabricante", "ValorVenda", "Ano"]]

# 3- Criando a tabela pivô
pivot_table = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)

print(pivot_table)

# 4- Exportando tabela pivô em excel
pivot_table.to_excel("data/pivot_table.xlsx", "Relatorio")