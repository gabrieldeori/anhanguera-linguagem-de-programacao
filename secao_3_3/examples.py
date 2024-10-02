import pandas as pd

from datetime import date
from datetime import datetime as dt

# Buscando dados de API
df_selic = pd.read_json('\https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json')
print(df_selic.info())

# Inserindo Dados
data_extracao = date.today()
df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = “Autor”


print(df_selic.info())
df_selic.head()

# Lendo Dados Específicos
df_selic.loc[0]

df_selic.loc[[0,20,70]]

# Testando valores
teste = df_selic['valor'] < 0.01
print(type(teste))
