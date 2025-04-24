import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

import plotly.graph_objs as go
import plotly.express as px

import pandas as pd
import numpy as np
# APIs dados financeiros
import yfinance as yf

# Criando o App
app = dash.Dash( 
    __name__, 

    # Incluir o frameworks de frontend
    external_stylesheets=[ 
        # Link dos estilos
        # https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
        # Setar o estilo
        dbc.themes.JOURNAL, 

        # Importar 
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css',
        'https://fonts.googleapis.com/css2?family=Joan&family=Roboto:ital,wght@0,100;1,300&family=Source+Sans+Pro:ital,wght@0,400;1,300&display=swap'
    ], 
    # Nome da Pagina
    title='Dashboard' 
)

# Criando o FrontEnd
app.layout = dbc.Container(
    
    # Pagina
    children=[

        # Linha da Barra de Navegação
        dbc.Row([

            # Barra de Navegação
            dbc.Navbar(

                # Container (DIV)
                dbc.Container(
                    [   
                        html.A(
                            
                            dbc.Row(
                                [
                                    dbc.Col(html.Img(src=app.get_asset_url('Icone.png'), height="50px")),
                                    dbc.Col(dbc.NavbarBrand('Dashboard Financeiro', className="ms-1") ),
                                ],
                                align='center', className='g-0',
                            ), href='#', style={'textDecoration': 'none'},
                        ),
                    ]
                ),
            ),
        ]),

        # Linha Seleção do formulário
        dbc.Row([ 

            # Titulo
            html.Div([
                
                # Titulo
                html.H6('Selecione um ação:')

                ], style={'margin-top': '15px' } 
            ),

            # Botão do formulário
            html.Div([

                # Div do combobox
                html.Div([
                    dcc.Dropdown(
                        id='opcao-dropdown',
                        options=[
                            {'label': 'Itaú', 'value': 'ITUB4.SA'},
                            {'label': 'Bradesco', 'value': 'BBDC4.SA'},
                            {'label': 'Santander', 'value': 'SANB11.SA'},
                            {'label': 'Inter', 'value': 'INBR32.SA'},
                            {'label': 'Tesla', 'value': 'TSLA34.SA'},
                        ],
                        value='ITUB4.SA'  # Valor inicial
                    ),
                ], style={'width':'250px', 'margin-right':'10px'} ),

                # Div do botão
                html.Div([
                ], style={'width':'250px'} )
                
            ], style={
                'display': 'inline-block', 
                'display':'flex',
                'width':'100%',
                'height':'70px',
                'align-items': 'center'
            } ),
          
        ]),

        html.H5( 'Análise dos indicadores', style={'margin-top':'15px'} ),

        # Gráfico principal
        dbc.Col([
            
            # Gráfico
            dcc.Loading(
                id='loading-1',
                type='default',
                children=[
                    dcc.Graph(
                        id='Grafico_Serie',
                        #figure=Figura,
                        style={'height':'80vh', 'margin-rigth':'0px'}
                    )
                ]
            ),
        ]),

        # Subs gráficos
        dbc.Row([

            #Coluna 1
            dbc.Col([

                # Gráfico
                dcc.Loading(
                    id='loading-2',
                    type='default',
                    children=[
                        dcc.Graph(
                            id='Grafico_Serie_02',
                            #figure=Grafico_02,
                            style={'height':'60vh', 'margin-rigth':'0px'}
                        )
                    ]
                ),
            ], md=6 ),

            #Coluna 2
            dbc.Col([

                # Gráfico
                dcc.Loading(
                    id='loading-3',
                    type='default',
                    children=[
                        dcc.Graph(
                            id='Grafico_Serie_03',
                            #figure=Grafico_03,
                            style={'height':'60vh', 'margin-rigth':'0px'}
                        )
                    ]
                ),
            ], md=6 ),
        ]),
    ]
)

### ### ### ### ### ###
### Funções BACKEND ###
### ### ### ### ### ###

def obter_dados_acao(ticker, data_inicio, data_fim):
    # Função para buscar a ação
    Acao = yf.download(ticker, start=data_inicio, end=data_fim)
    return Acao

def calcular_ganho_hipotetico(Acao):
    # Função para calcular o ganho
    preco_compra = Acao['Close'].iloc[0]
    preco_venda = Acao['Close'].iloc[-1]
    ganho_hipotetico = preco_venda - preco_compra
    return ganho_hipotetico

# Parametros para a busca
Data_inicio = '2022-01-01'
Data_fim = '2023-08-15'

# Métricas da média
media_movel_curta=20
media_movel_longa=50

@app.callback(
    Output('Grafico_Serie', 'figure'),
    Input('opcao-dropdown', 'value'))
def update_graph(opcao_dropdown):

    # Chamando as funções
    Dados_API = obter_dados_acao(opcao_dropdown, Data_inicio, Data_fim)
    Ganho_Perda = calcular_ganho_hipotetico( Dados_API )

    # Cria o gráfico interativo de linha
    Figura = go.Figure()

    Figura.add_trace(
        go.Scatter(
            x=Dados_API.index,
            y=Dados_API['Close'],
            mode='lines',
            name=f'Preço de Fechamento - {opcao_dropdown}'
        )
    )

    Figura.add_trace(
        go.Scatter(
            x=Dados_API.index,
            y=Dados_API['Close'].rolling(window=media_movel_curta).mean(),
            mode='lines',
            name=f'Média Móvel {media_movel_curta} períodos',
            line=dict(color='orange')
        )
    )

    Figura.add_trace(
        go.Scatter(
            x=Dados_API.index,
            y=Dados_API['Close'].rolling(window=media_movel_longa).mean(),
            mode='lines',
            name=f'Média Móvel {media_movel_longa} períodos',
            line=dict(color='red')
        )
    )

    Figura.update_traces(
        hoverinfo='x+y',
        hovertemplate='Data: %{x} <br>Valor: %{y:.2f}'
    )

    Figura.update_layout(
        title=f'Preço de Fechamento da Ação {opcao_dropdown}',
        xaxis_title='Data',
        yaxis_title='Preço de Fechamento',
        showlegend=True,
        hovermode='x',
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
        plot_bgcolor='#f5f5f5',
        font=dict(family='Arial', size=12, color='black'),
        margin=dict(l=50, r=50, t=80, b=50),
    )

    Figura.add_annotation(
        x=Dados_API.index[-1],
        y=Dados_API['Close'].iloc[-1],
        text=f'Ganho Hipotético: ${Ganho_Perda:.2f}',
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

    Figura.add_annotation(
        x=Dados_API.index[0],
        y=Dados_API['Close'].iloc[0],
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

    return Figura




if __name__ == '__main__':
    app.run_server( debug=True )