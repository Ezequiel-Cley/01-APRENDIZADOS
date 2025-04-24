import yfinance as yf
import pandas as pd

# Estudo da Apple

# Variaveis
Ticker = 'AAPL'
Data_Inicio = '2022-01-01'
Data_Fim = '2023-01-01'

# Função para buscar os dados
def obter_dados_acao( ticker, data_inicio, data_fim):

  # Requisão
  Acao = yf.download( ticker, data_inicio, data_fim )

  return Acao

# Buscar os dados da Apple
Dados_Apple = obter_dados_acao(Ticker, Data_Inicio, Data_Fim )

# Verificar
Dados_Apple.head()

type(Dados_Apple)

Dados_Apple.info()

Dados_Apple.describe()

Dados_Apple.reset_index().sort_values( by='Date', ascending=False )

# Calcular o ganho
def Calcular_Ganho( Acao ):

  # Preço compra (Quanto eu comprei)
  Preco_Compra = Dados_Apple['Close'].iloc[0]

  # Preço de venda (Quando teria vendido)
  Preco_Venda = Dados_Apple['Close'].iloc[-1]

  # Calculo
  Ganho = Preco_Venda - Preco_Compra

  return Ganho

# Funcao
Ganho_Perda = Calcular_Ganho( Dados_Apple )

# Ganhei ou perdi ?
Ganho_Perda

# Analise
Dados_Apple['Close'].iloc[0], Dados_Apple['Close'].iloc[-1]

import plotly.graph_objects as go

# Medias Moveis
Media_movel_curta = 20
Media_movel_longa = 50

# Criar uma figura
Figura = go.Figure()

# Adicionar gráfico
Figura.add_trace(

  # Escolhendo o gráfico
  go.Scatter(

      # Eixo x
      x=Dados_Apple.index,

      # Eixo Y
      y=Dados_Apple.Close,

      # Tipo do gráfico
      mode='lines',

      # Nome
      name=f'Preço de fechamento - {Ticker}'
  )

)

# Adicionar Média Móvel
Figura.add_trace(

  # Escolhendo o gráfico
  go.Scatter(

      # Eixo x
      x=Dados_Apple.index,

      # Eixo Y
      y=Dados_Apple.Close.rolling( window=Media_movel_curta).mean(),

      # Tipo do gráfico
      mode='lines',

      # Nome
      name=f'Média móvel {Media_movel_curta} períodos',

      # Cor da linha
      line= dict( color='orange' )
  )

)


# Adicionar Média Móvel
Figura.add_trace(

  # Escolhendo o gráfico
  go.Scatter(

      # Eixo x
      x=Dados_Apple.index,

      # Eixo Y
      y=Dados_Apple.Close.rolling( window=Media_movel_longa).mean(),

      # Tipo do gráfico
      mode='lines',

      # Nome
      name=f'Média móvel {Media_movel_longa} períodos',

      # Cor da linha
      line= dict( color='red' )
  )

)

# Mexer no Layout
Figura.update_layout(

  # Titulo
  title=f'Preço de Fechamento da Ação {Ticker}',

  # Label x
  xaxis_title='Data',

  # Label y
  yaxis_title='Preço de Fechamento',

  # Mostrar legendas
  showlegend=True,

  # Ajuste da Legenda
  legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1 ),

  # Cor de fundo
  plot_bgcolor='rgba(240, 240, 240, 0.95)',

  # Fonte e tamanhao do texto
  font=dict(family='Arial', size=12, color='black'),

  # Margin
  margin=dict(l=50, r=50, t=80, b=50),

  # Mostra banner
  hovermode='x',

)

# Adicionando tooltips interativos
Figura.update_traces(

    # Incluindo dados do eixo x e y
    hoverinfo='x+y',

    # Mostrar a informação
    hovertemplate='Data: %{x} <br>Valor: %{y:.2f}'
)

# Adicionar anotação
Figura.add_annotation(

  # Posição x da anotação (última data)
  x=Dados_Apple.index[-1],

  # Posição y da anotação (preço de fechamento na última data)
  y=Dados_Apple['Close'].iloc[-1],

  # Texto da anotação com o valor do ganho
  text=f'Ganho Hipotético: ${Ganho_Perda:.2f}',

  # Exibir uma seta apontando para o ponto
  showarrow=True,

  # Estilo da seta
  arrowhead=2,

  # Ajuste da posição horizontal do texto (0 = centro)
  ax=0,

  # Ajuste da posição vertical do texto (-40 = acima do ponto)
  ay=-40,

  # Cor da seta
  arrowcolor='black',

  # Espessura da seta
  arrowwidth=2,

  # Cor da borda da caixa de texto
  bordercolor='gray',

  # Espessura da borda da caixa de texto
  borderwidth=1,

  # Cor de fundo da caixa de texto
  bgcolor='lightgray',

  # Opacidade da caixa de texto
  opacity=0.8

)

Figura.add_annotation(
        x=Dados_Apple.index[0],
        y=Dados_Apple['Close'].iloc[0],
        xref='x',
        yref='y',
        text='Comprei',
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-40,
        arrowcolor='black',
        arrowwidth=2,
        bordercolor='gray',
        borderwidth=1,
        bgcolor='lightgray',
        opacity=0.8
    )

# Mostrando
Figura.show()

Dados_Apple['Close']