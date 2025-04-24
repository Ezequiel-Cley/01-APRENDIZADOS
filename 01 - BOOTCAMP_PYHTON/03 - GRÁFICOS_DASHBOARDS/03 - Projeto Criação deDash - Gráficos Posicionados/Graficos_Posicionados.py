# PROJETO CRIAÇÃO DE DASH - GRÁFICOS POSIONADOS

# Libs
import pandas as pd
import numpy as np

# plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Avisos
import warnings
warnings.filterwarnings('ignore')

# Configurar o número de casas decimais para 2
pd.options.display.float_format = '{:.2f}'.format

# Carregar os dados
Base_Dados = pd.read_csv('glp-2022-02.csv', sep=';')

# Verificar
Base_Dados.head()

# Analisa base de dados
def Verificar_DataSet(Base_Dados ):

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


Verificar_DataSet( Base_Dados )

# Ajuste Nome_Colunas
Base_Dados.columns = [ Coluna.lower().replace('-', '').replace(' ', '_') for Coluna in Base_Dados.columns ]

Base_Dados.columns

# Ajuste coluna valor
Base_Dados.valor_de_venda = Base_Dados.valor_de_venda.apply( lambda valor: valor.replace(',' , '.') )
Base_Dados.valor_de_venda = pd.to_numeric( Base_Dados.valor_de_venda )
Base_Dados.valor_de_venda.dtypes

# Convertendo as datas
Base_Dados.data_da_coleta = pd.to_datetime( Base_Dados.data_da_coleta, format='%d/%m/%Y' )
Base_Dados['Mes'] = Base_Dados.data_da_coleta.dt.month
Base_Dados['Ano'] = Base_Dados.data_da_coleta.dt.year

Base_Dados.head()

# Publico Executivo | Amplo
# Serie Temporal da media do preço BRASIL
# Acompanhar Oscilação Preço / %
# Visão dos Estados

# Criando a analise média Brasil
Anl_Media_BR = Base_Dados.groupby( by='Mes' ).agg(
    Media = ('valor_de_venda', 'mean')
).reset_index()

Anl_Media_BR.head()

# Calculando a oscilação do preço anterior do mes atual
Anl_Oscilacao_Preco = (Base_Dados.groupby( by='Mes' ).agg(
    Media = ('valor_de_venda', 'mean')
).reset_index()['Media'] - Base_Dados.groupby( by='Mes' ).agg(
    Media = ('valor_de_venda', 'mean')
).reset_index()['Media'].shift(1)).reset_index()

# Verificando
Anl_Oscilacao_Preco.head()

# Calculando a oscilação do preço anterior do mes atual
Anl_Oscilacao_Percentual = ((Base_Dados.groupby( by='Mes' ).agg(
    Media = ('valor_de_venda', 'mean')
).reset_index()['Media'] / Base_Dados.groupby( by='Mes' ).agg(
    Media = ('valor_de_venda', 'mean')
).reset_index()['Media'].shift(1) - 1) * 100 ).reset_index()

# Verificando
Anl_Oscilacao_Percentual.head()


# Criar um grid de gráficos
Figura = make_subplots(

    # Layout do relatorio
    rows=4, cols=5,

    # Design
    specs=[

      # 1 linha
      [ { 'colspan': 3, 'rowspan' : 2 }, None, None, { 'colspan' : 2 }, None ],

      # 2 linha
      [ None, None, None, { 'colspan' : 2 }, None ],

      # 3 linha
      [ { 'colspan': 5, 'rowspan' : 2 }, None, None, None, None ],

      # 4 linha
      [ None, None, None, None, None ],

    ],

    # Titulos
    #subplot_titles=( [Loop for Loop in range(1, 21)] )
    subplot_titles=( 'Média preço de venda GLP, Brasil', 'Oscilação preço', 'Percentual oscilação preço', 'Análise preço por estados' )

)

Figura


Azul = 'rgb(49,130,189)'

# Criando o gráfico 1
Grafico_1 = go.Scatter(
    x=Anl_Media_BR.Mes,
    y=Anl_Media_BR.Media,
    mode='lines',
    name='Serie Temporal Brasil',
    line=dict(width=5, color=Azul)
)

# Criando o gráfico 2
Grafico_2 = go.Scatter(
    x=Anl_Oscilacao_Preco.index,
    y=Anl_Oscilacao_Preco.Media,
    mode='lines+markers',
    name='Oscilação de preço',
    line=dict(width=2, color='rgb(46, 67, 46)')
)

# Criando o gráfico 3
Grafico_3 = go.Scatter(
    x=Anl_Oscilacao_Percentual.index,
    y=Anl_Oscilacao_Percentual.Media,
    mode='lines+markers',
    name='Oscilação de preço',
    line=dict(width=2, color='rgb(46, 67, 46)')
)

# Criando o gráfico 4
Grafico_4 = go.Heatmap(
    x=Base_Dados.estado__sigla,
    y=Base_Dados.Mes,
    z=Base_Dados.valor_de_venda,
    colorscale=[
        [0.0, 'rgb(67,67,67)'],
        [0.3, 'rgb(115,115,115)'],
        [0.6, 'rgb(189,189,189)'],
        [1.0, 'rgb(49, 189, 94)']
    ],
    showscale=False,
    texttemplate='%{z}'
)

# Adicionado os gráficos no relatorio
Figura.add_trace( Grafico_1, row=1, col=1 )
Figura.add_trace( Grafico_2, row=1, col=4 )
Figura.add_trace( Grafico_3, row=2, col=4 )
Figura.add_trace( Grafico_4, row=3, col=1 )

### ### ### ### ### ###
### Customatização ###
### ### ### ### ### ###

# Ajuste na Figura
Figura.update_layout(
    # Tamanhos
    width=1200, height=1000,

    # Titulo geral
    title='Estudo preço do GLP 2022'
)

Figura.update_traces(
    # Desativas Legendas
    showlegend=False
)

###
# Ajustar o gráfico 1
###

# Loop para inserir um ponto na linha de cada valor
for x, y in zip( Anl_Media_BR.Mes, Anl_Media_BR.Media ):

  # Adicionado ponto a ponto na linha
  Figura.add_trace(
      go.Scatter(
          # Valores
          x=[x], y=[y + 0.5],

          # Texto dos valores x e y
          mode='text',

          # Texto que vai mostrar
          text=[ f'{ round(y) }' ],

          # Desativar lengeda
          showlegend=False
      )
  )

# Ajustar o eixo Y
Figura.update_yaxes(
    # Titulo
    title_text='Valor em reais R$',

    # Linhas de grade
    showgrid=False,

    # Não mostra a linha zero
    showline=True,

    # Mostrar os rotulos
    showticklabels=True,

    # Distância do título em relação ao eixo (em pixels)
    title_standoff=2,

    # Ajuste da Fonte
    tickfont=dict( family='Arial', size=10, color='rgb(82, 82, 82)'),

    # Eixo do Range
    range=[ 100, 120 ],

    # Apontar para onde vai esse ajuste
    row=1, col=1
)

# Ajuste eixo X
Figura.update_xaxes(

    # titulo
    title_text='Período mensal',

    # Linhas e valores
    showline=True, showgrid=False, showticklabels=True,

    # Cores
    linecolor='rgb(204, 204, 204)', linewidth=3,

    # Fora
    ticks='outside',

    # Cor e layout da fonte
    tickfont=dict( family='Arial', size=12, color='rgb(82, 82, 82)'),

    # Posição
    row=1, col=1
)

###
# Ajustar o gráfico 2
###

# Ajustar o eixo Y
Figura.update_yaxes(
    # Titulo
    title_text='R$',

    # Linhas de grade
    showgrid=False,

    # Não mostra a linha zero
    showline=True,

    # Mostrar os rotulos
    showticklabels=True,

    # Distância do título em relação ao eixo (em pixels)
    title_standoff=2,

    # Ajuste da Fonte
    tickfont=dict( family='Arial', size=10, color='rgb(82, 82, 82)'),

    # Eixo do Range
    range=[ -5, 10 ],

    # Apontar para onde vai esse ajuste
    row=1, col=4
)

# Ajuste eixo X
Figura.update_xaxes(

    # titulo
    title_text='Período',

    # Linhas e valores
    showline=True, showgrid=False, showticklabels=True,

    # Cores
    linecolor='rgb(204, 204, 204)', linewidth=1,

    # Fora
    ticks='outside',

    # Cor e layout da fonte
    tickfont=dict( family='Arial', size=12, color='rgb(82, 82, 82)'),

    # Posição
    row=1, col=4
)

###
# Ajustar o gráfico 3
###

# Ajustar o eixo Y
Figura.update_yaxes(
    # Titulo
    title_text='%',

    # Linhas de grade
    showgrid=False,

    # Não mostra a linha zero
    showline=True,

    # Mostrar os rotulos
    showticklabels=True,

    # Distância do título em relação ao eixo (em pixels)
    title_standoff=2,

    # Ajuste da Fonte
    tickfont=dict( family='Arial', size=10, color='rgb(82, 82, 82)'),

    # Eixo do Range
    range=[ -5, 10 ],

    # Apontar para onde vai esse ajuste
    row=2, col=4
)

# Ajuste eixo X
Figura.update_xaxes(

    # titulo
    title_text='Período',

    # Linhas e valores
    showline=True, showgrid=False, showticklabels=True,

    # Cores
    linecolor='rgb(204, 204, 204)', linewidth=1,

    # Fora
    ticks='outside',

    # Cor e layout da fonte
    tickfont=dict( family='Arial', size=12, color='rgb(82, 82, 82)'),

    # Posição
    row=2, col=4
)

'''Figura.update_layout(
  annotations=[
    dict(
      xref='paper', yref='paper', x=0.5, y=-0.04,
      xanchor='center', yanchor='top',
      text='Fonte dos dados: Gov.BR',
      font=dict(family='Arial', size=15, color='rgb(75, 75, 75)'),
      showarrow=False)
  ]
)'''

Figura

# Exportar figura
Figura.write_image('Relatorio.pdf')

# Biblioteca necessaria para torna seu realtório em PDF
#!pip install -U kaleido