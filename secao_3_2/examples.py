import pandas as pd

# Criando uma lista de valores
data = [10, 20, 30, 40, 50]

# Criando uma Series a partir da lista
series1 = pd.Series(data)

print(series1)


# Criando um dicionário com pares chave-valor
data = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}

# Criando uma Series a partir do dicionário
series2 = pd.Series(data)

print(series2)


# Lendo dados em páginas html
url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))

df_bancos = dfs[0]

print(df_bancos.shape)
print(df_bancos.dtypes)

df_bancos.head()
