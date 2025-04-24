# Modelagem de Dados - 

# Bibliotecas para modelagem
import pandas as pd
import numpy as np

# Bibliotecas para Visualização
import plotly.express as px
import plotly.graph_objects as go

# Avisos
import warnings

# Ignorar avisos
warnings.filterwarnings('ignore')

# Parametros para mostar colunas no pandas
pd.set_option('display.max_columns', None)

# Ler os dados
Base_Dados = pd.read_csv('Airbnb_Open_Data.csv')

# Dimensão
Base_Dados.shape

# Colunas
Base_Dados.columns

# Informações
Base_Dados.info()

# Tipos das colunas
Base_Dados.dtypes

# Valores unicos
Base_Dados.nunique()

# Campos nulos
Base_Dados.isnull().sum()

# Estatísticas básicas
Base_Dados.describe().transpose()

# Estatísticas básicas - Categoricos
Base_Dados.describe( include=['O'] ).transpose()

# Correlação
Base_Dados.corr()

# Problema colunas com espaços
Base_Dados.columns

# Ajustar coluna
for loop in Base_Dados.columns:
  print( loop.lower().replace(' ', '_') )
  
  # Experimento
[ Coluna.lower().replace(' ', '_') for Coluna in Base_Dados.columns ]

# Renomear
Base_Dados.columns = [ Coluna.lower().replace(' ', '_') for Coluna in Base_Dados.columns ]

# Verificar
Base_Dados.columns

# Calcular o % de campos nulos
Percentual = Base_Dados.isnull().sum() / Base_Dados.shape[0] * 100

# Dicionario
Dicionario = {
    'Colunas' : Percentual.keys(),
    '%_Nulos' : Percentual
}

# Criar um DataFrame
Resultado_Percentual = pd.DataFrame( Dicionario )

# Resetar o index
Resultado_Percentual.reset_index( drop=True, inplace=True )

# Ordenar
Resultado_Percentual.sort_values( by='%_Nulos' )

# Colunas para retirar
Lista_Colunas = ['id', 'host_id']

# Aplicando função
Base_Dados.drop( columns=Lista_Colunas, axis=1, inplace=True )

# Analise
Base_Dados.country.unique()

# Remover as colunas
Lista_Colunas_2 = ['country_code', 'country']

# Aplicando função
Base_Dados.drop( columns=Lista_Colunas_2, axis=1, inplace=True )

# Memoria
Base_Dados.info()

# Problema de String em Valor
Base_Dados.price.head()

# Campos vazios
Base_Dados.price.isnull().sum()

# Função
def Remover_Sifrao( Valor ):

  # Caso seja nulo
  if pd.isna( Valor ):
    return np.NAN

  # Caso não seja, trate o valor
  else:

    # remover o $
    Nova_Registro = Valor.replace('$', '')

    # Remover ',' - '.'
    Nova_Registro = Nova_Registro.replace(',', '.')

    # Remover Espaços '  '
    Nova_Registro = Nova_Registro.replace(' ', '')

    return float( Nova_Registro )

# Aplicar a função
Base_Dados.price = Base_Dados.price.apply( Remover_Sifrao )

# Tipo
Base_Dados.price.dtypes

# Função
for loop in Base_Dados.price.head():
  print( loop )
  
# Coluna Data
Base_Dados.last_review

# Converter para Data
#Base_Dados.last_review = pd.to_datetime( Base_Dados.last_review, format='%Y%m%d', errors='ignore' )
Base_Dados.last_review = pd.to_datetime( Base_Dados.last_review )

# Verificando
Base_Dados.last_review.dtypes

# Verificando campos duplicados
Base_Dados.shape, Base_Dados.drop_duplicates().shape

# Aplique no DataSet
Base_Dados.drop_duplicates( keep='first', inplace=True )

# Visualizar partes do dataset
Base_Dados.iloc[ 2:5, 1:5 ]

Base_Dados.iloc[ -5:-2, 5:10 ]

# Agrupar
Base_Dados.groupby( by='neighbourhood_group' ).describe()

# Analise de Bairro , Quantidade e Média de Preço
Base_Dados.groupby( by='neighbourhood_group' ).agg(

  # Contar
  Quantidade = ('name', 'count'),

  # Média
  Media = ('price', 'mean')

)

# Ajustar os dados no Data Frame
Base_Dados.loc[ Base_Dados.neighbourhood_group == 'brookln' ]

# Corrigir o nome
Base_Dados.iloc[13, 3] = 'Brooklyn'

# Ajustar os dados no Data Frame
Base_Dados.loc[ Base_Dados.neighbourhood_group == 'manhatan' ]

# Corrigir o nome
Base_Dados.iloc[18, 3] = 'Manhattan'

# Analise de Bairro , Quantidade e Média de Preço
Base_Dados.groupby( by='neighbourhood_group' ).agg(

  # Contar
  Quantidade = ('name', 'count'),

  # Média
  Media = ('price', 'mean')

)

# Price
Base_Dados.loc[ Base_Dados.price.isnull() ].head(2)

# Colocando a média nos campos nulos
Base_Dados.price.fillna( Base_Dados.price.mean(), inplace=True )

# Verificando
Base_Dados.price.isnull().sum()

# PX
px.box( Base_Dados, y='price', x='neighbourhood_group', color='neighbourhood_group', title='Bairro x Preço' )

# Mapa de Calor - GO
Analise_Mapa = go.Figure(

  # Dados
  data=go.Densitymapbox(

      # Dados geolocalização
      lat = Base_Dados['lat'],
      lon = Base_Dados['long'],

      # Valor
      z = Base_Dados['price'],

      # Extensão do calor
      radius=1,

      # Segmento por bairro
      customdata = Base_Dados['neighbourhood_group'],
      hovertemplate = '<b>Preço:</b> %{z}<br><b>Bairro:</b> %{customdata}'
  )
)

Analise_Mapa.update_layout(

  # estilo do mapa
  mapbox_style='stamen-terrain',

  # Centralização
  mapbox_center_lon = -73.97237,
  mapbox_center_lat = 40.64749,

  # Zoom
  mapbox_zoom=8

)

Analise_Mapa.show()