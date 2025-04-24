# Iniciação em Criação de Gráficos

# Libs
import pandas as pd
import numpy as np

# Modulos do Plotly
import plotly.express as px

# Avisos
import warnings
warnings.filterwarnings('ignore')

# Configurar o número de casas decimais para 2
pd.options.display.float_format = '{:.2f}'.format

# Lendo a base de dados
Base_Dados = pd.read_csv('ca-2022-02.csv', sep=';')

# Verificando
Base_Dados.head()

# Analisa base de dados
def Verificar_DataSet( Base_Dados ):

  # Verificando dimensão
  Dimensao = Base_Dados.shape
  print(f'Base de dados possui { Dimensao[0] } Linhas e {Dimensao[1] } Colunas')
  print('-' * 50 )

  # Tipo das Colunas
  Tipos_Colunas = Base_Dados.dtypes.value_counts()
  print(f'Tipo das colunas')
  print( pd.DataFrame( Tipos_Colunas, columns=['Quantidade_Colunas'] ) )
  print('-' * 50 )

  # Campos únicos
  Campos_Unicos = Base_Dados.nunique()
  print(f'Campos únicos')
  print( pd.DataFrame( Campos_Unicos, columns=['Quantidade_Campos'] ) )
  print('-' * 50 )

  # Campos nulos
  Campos_Nulus = Base_Dados.isnull().sum()
  print(f'Campos Nulos')
  print( pd.DataFrame( Campos_Nulus, columns=['Quantidade_Campos'] ) )
  print('-' * 50 )

# Chamando a função
Verificar_DataSet(Base_Dados)

# Ajuste das colunas
Base_Dados.columns = [ Coluna.lower().replace('-', '').replace(' ', '_') for Coluna in Base_Dados.columns ]
Base_Dados.columns

# Ajuste do valor
Base_Dados.valor_de_venda = Base_Dados.valor_de_venda.apply( lambda valor: valor.replace(',', '.') )
Base_Dados.valor_de_venda = pd.to_numeric( Base_Dados.valor_de_venda )
Base_Dados.valor_de_venda.dtypes

# Ajuste na Data
Base_Dados.data_da_coleta = pd.to_datetime( Base_Dados.data_da_coleta, format='%d/%m/%Y' )
Base_Dados['Mes'] = Base_Dados.data_da_coleta.dt.month
Base_Dados['Ano'] = Base_Dados.data_da_coleta.dt.year

# VErificando
Base_Dados.head()

Base_Dados['regiao__sigla'].unique()

Base_Dados['estado__sigla'].unique()

Base_Dados['produto'].unique()

# Filtrar o estado de SP
Filtro_SP = Base_Dados[
  ( Base_Dados['estado__sigla'] == 'SP' ) &
  ( Base_Dados['produto']=='GASOLINA' )
]

Filtro_SP.head(2)

# Analise da Média
Anl_Media = Filtro_SP.groupby( by=['Mes'] ).agg(
    Media = ('valor_de_venda', 'mean'),
    Mediana = ('valor_de_venda', 'median')
).reset_index()

Anl_Media

# Gráficos de Linhas
px.line( Anl_Media, x='Mes', y='Media' )

# Gráfico de Linhas
Figura_Linhas = px.line(
    Anl_Media, x='Mes', y='Media',
    title='Preço medio gasolina no estado de SP',
    text='Media',
    markers=True,
    height=500, width=1000,
    labels={'Mes':'2º Semestre de 2022', 'Media':'Preço médio de venda R$' }
)

# Ajustar a construção do gráfico
Figura_Linhas.update_traces(
    hovertemplate='Mes: %{x} <br>Preço Médio: R$ %{y:.2f}',
    texttemplate='R$ %{y:.2f}', textposition='top center',
    fill='tozeroy',
    fillcolor='rgba(198, 213, 245, 0.5)',
    textfont=dict(size=13, color='blue', family='Arial')
)

# Ajustar o Layout
Figura_Linhas.update_layout(
    xaxis_range=[6.8, 12.2],
    yaxis_range=[0, Anl_Media.Media.max() + ( Anl_Media.Media.max() * 0.25 ) ],
    xaxis_showgrid=False,
    plot_bgcolor='#f2f5fa',
)

Figura_Linhas.show()

# Gráfico de Barras
Figura_Barras = px.bar( Anl_Media, x='Mes', y='Mediana', title='Gráfico de Barras' )

Figura_Barras.show()

# Scatter Plot
Anl_Produto = Base_Dados[ Base_Dados.estado__sigla == 'SP' ].pivot_table( index=['municipio'], columns='produto', values='valor_de_venda').reset_index()

# Verificar
Anl_Produto.head()

# Scatter Plot
px.scatter(Anl_Produto, x='GASOLINA', y='ETANOL' )

px.scatter(Anl_Produto, x='GASOLINA', y='ETANOL', title='Comparação Gasolina x Etanol',
           trendline='ols', trendline_color_override='darkred',
           height=600,  width=1000 )
		   
Anl_Produto.corr()

Figura_Calor = px.imshow( Anl_Produto.corr(), title='Correlação entre os combustíveis', text_auto=True, aspect='auto'  )
Figura_Calor.update_xaxes(side='top')
Figura_Calor.show()

# Boxplot
px.box(
    Base_Dados, x='regiao__sigla', y='valor_de_venda',
    color='produto', title='Distribuição combustíveis por Região')
	
# Calculando os %
Anl_Represetnacao = Base_Dados.produto.value_counts( normalize=True ).reset_index()

px.pie( Anl_Represetnacao, names='index', values='produto', title='Gráfico de Pizza' )

Figura_Pizza = px.pie( Anl_Represetnacao, names='index', values='produto', title='Gráfico de Pizza', hole=0.6 )

Figura_Pizza.update_traces(
    hoverinfo='label+percent', textinfo='percent+label', textfont_size=12,
    textposition='inside',
    marker=dict( line=dict(color='#ffffff', width=2) ) )

Figura_Pizza.add_annotation(
    x=0.5, y=0.5,
    text=f'{ round(Base_Dados.shape[0] / 1000) } mi ',
    showarrow=False,
    font=dict(
        size=22,
        color='black'
    )
)

Figura_Pizza.show()

px.histogram( Anl_Produto, x='GASOLINA', title='Gráfico de Histograma')

Base_Dados.head(2)

Base_Dados.produto.unique()

# Analise dos estados
Anl_Estados = Base_Dados[ Base_Dados.produto == 'ETANOL' ].groupby( by=['estado__sigla'] ).agg(
    Media = ('valor_de_venda', 'mean')
).reset_index()

Anl_Estados.head()

sigla_codigo_map = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AM': 'Amazonas',
    'AP': 'Amapá',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piaui',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondonia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}

estados_coords = {
    'Acre': (-9.0238, -70.8120),
    'Alagoas': (-9.5713, -36.7819),
    'Amazonas': (-3.4168, -65.8561),
    'Amapá': (1.4315, -51.7717),
    'Bahia': (-12.5797, -41.7007),
    'Ceará': (-5.4984, -39.3206),
    'Distrito Federal': (-15.7998, -47.8645),
    'Espírito Santo': (-19.1834, -40.3089),
    'Goiás': (-16.6410, -49.3659),
    'Maranhão': (-4.9609, -45.2744),
    'Mato Grosso': (-12.6819, -56.9211),
    'Mato Grosso do Sul': (-20.7722, -54.7852),
    'Minas Gerais': (-18.5122, -44.5550),
    'Pará': (-3.4168, -52.1013),
    'Paraíba': (-7.24, -36.7819),
    'Paraná': (-24.89, -51.1557),
    'Pernambuco': (-8.8137, -36.9541),
    'Piaui': (-6.6033, -42.2796),
    'Rio de Janeiro': (-22.9068, -43.1729),
    'Rio Grande do Norte': (-5.4026, -36.9541),
    'Rio Grande do Sul': (-30.0346, -51.2177),
    'Rondonia': (-11.5057, -63.5806),
    'Roraima': (2.7376, -62.0751),
    'Santa Catarina': (-27.2423, -50.2189),
    'São Paulo': (-23.5505, -46.6333),
    'Sergipe': (-10.5741, -37.3857),
    'Tocantins': (-10.1753, -48.2982)
}

# Enriquecendo os dados
Anl_Estados['Estado'] = Anl_Estados['estado__sigla'].map( sigla_codigo_map )

Anl_Estados['Latitude'] = Anl_Estados['Estado'].map( lambda estado: estados_coords[estado][0] )
Anl_Estados['Longitude'] = Anl_Estados['Estado'].map( lambda estado: estados_coords[estado][1] )

Anl_Estados.head()

Grafico_Mapa = px.density_mapbox(
    Anl_Estados,
    lat='Latitude',
    lon='Longitude',
    z='Media',
    hover_data=['Estado', 'Media'],
    mapbox_style='open-street-map',
    radius=25,
    center=dict(lat=-15.80, lon=-47.86),
    zoom=3
)

Grafico_Mapa.update_layout(
    margin={'r':0,'t':0,'l':0,'b':0},
    coloraxis_showscale=False )

Grafico_Mapa.show()

Base_Dados.columns

#Desafio

#1. Escolha um estado e busque a Geo Localização de cada cidade
#2. Faça um mapa de calor
#3. Marque o Data Viking, Odemir Depieri e Ronisson Lucas

import requests

def get_coordinates(city, state):

  '''
    Função para buscar a Geo Localizacao
  '''

   # Site para buscar a Geo localização
  Url = f'https://nominatim.openstreetmap.org/search'

  # Parametros para enviar os dados na API
  Parametros = {
      'q': f'{city}, {state}',
      'format': 'json',
  }

  # Fazendo a requisição
  Resposta = requests.get( Url, params=Parametros )

  # Retorno
  Dados_Retorno = Resposta.json()

  # Validando se há valor na resposta
  if Dados_Retorno and len(Dados_Retorno) > 0:

    # Extraindo os valores
    latitude = float(Dados_Retorno[0]['lat'])
    longitude = float(Dados_Retorno[0]['lon'])

    # Retorno
    return latitude, longitude

  else:
     return None
	 
get_coordinates( 'Curitiba', 'Parana' )