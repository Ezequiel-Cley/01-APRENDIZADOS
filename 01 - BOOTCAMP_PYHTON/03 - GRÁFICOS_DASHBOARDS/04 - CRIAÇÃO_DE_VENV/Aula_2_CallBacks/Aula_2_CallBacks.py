import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np
import random

# Libs para gerar o PDF
import plotly.io as pio
import plotly.express as px
from flask import send_file
from dash.exceptions import PreventUpdate

### ### ### ### ### 
# Dados Sinteticos
### ### ### ### ### 

# Função para gerar dados aleatorios
def gerar_dados_aleatorios(num_linhas):

    # Lista
    dados = []

    # Loop para gerar dados
    for _ in range(num_linhas):

        # Geração dos dados
        idades = np.random.normal(loc=35, scale=10, size=num_linhas).astype(int)
        salarios = np.random.lognormal(mean=8.517193, sigma=0.434294, size=num_linhas)
        risco_credito = [ random.randint(0, 100) for _ in range(num_linhas)]
        score_serasa = np.random.normal(loc=750, scale=50, size=num_linhas)
        anos = [random.randint(2019, 2023) for _ in range(num_linhas)]
        
        # Consolidando os dados
        dados = list( zip(idades, salarios, risco_credito, score_serasa, anos) )

    return dados

# Criando o DF
# Altere o valor para a quantidade de linhas desejada
num_linhas = 100 # Quantidade registros aleatorios
dados_aleatorios = gerar_dados_aleatorios(num_linhas) # Chamando a função

# Construindo o DF
df = pd.DataFrame(
    dados_aleatorios, 
    columns=['Idade', 'Salario', 'Risco_Credito', 'Score_Serasa', 'anos']
)

# Busco o nome das coolunas
features = df.columns

print( features )

# Instanciamos nossa Aplicação
app = dash.Dash()

### ### ### ### 
# FRONTEND #
### ### ### ###
app.layout = html.Div([
    
    # Titulo
    html.H1('Análise dinâmica com 2 eixos'),

    # Div
    html.Div([

        # ComboBox
        dcc.Dropdown(
            id='xaxis',
            options=[{'label': i.title(), 'value': i} for i in features],
        ),

        # Flag do Eixo
        dcc.RadioItems(
            id='xaxis-type',
            options=[ {'label': Loop, 'value': Loop} for Loop in ['Linear', 'Log'] ],
            value='Linear',
            labelStyle={'display': 'inline-block', 'margin-top':'5px'}
        )
    ],

    # Estilo
    style={'width': '45%', 'display': 'inline-block'}),

    # Div lado esquerno
    html.Div([

        # Combo Box
        dcc.Dropdown(
            id='yaxis',
            options=[{'label': i.title(), 'value': i} for i in features],
        ),

        # Flag da escala do eixo
        dcc.RadioItems(
            id='yaxis-type',
            options=[{'label': Loop, 'value': Loop} for Loop in ['Linear', 'Log']],
            value='Linear',
            labelStyle={'display': 'inline-block', 'margin-top' : '5px'}
        )
    ],style={'width': '45%', 'float': 'right', 'display': 'inline-block'}),

    # Gráfico
    dcc.Graph(id='feature-graphic'),

    # Barra do Ano
    dcc.Slider(
        id='year--slider',
        min=df['anos'].min(),
        max=df['anos'].max(),
        value=df['anos'].median(),
        step=None,
        marks={ str(year): str(year) for year in df['anos'].unique() }
    ),

    html.Div([
        html.Button('Exportar PDF', id='export-pdf-button', style={'background-color': 'red', 'color': 'white'}, n_clicks=0),
        dcc.Location(id='url', refresh=True)
    ]),

] , style={ 'padding': 10 }  )

### ### ### ### 
# BACKEND #
### ### ### ###

# Função para atualizar os gráficos na pagina
@app.callback(
    Output('feature-graphic', 'figure'),
    [
        Input('xaxis', 'value'),
        Input('yaxis', 'value'),
        Input('xaxis-type', 'value'),
        Input('yaxis-type', 'value'),
        Input('year--slider', 'value')
    ])
def update_graph(xaxis_name, yaxis_name, xaxis_type, yaxis_type, year_value):

    # Filtrar os dados
    Filtro = df[ df['anos'] == year_value]

    # Condição se o usuário preencheu
    if xaxis_name and yaxis_name:
    
        return {
            
            'data': [go.Scatter(
                x=Filtro[xaxis_name],
                y=Filtro[yaxis_name],
                mode='markers',
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'line': {'width': 0.5, 'color': 'white'}
                }
            )],

            'layout': go.Layout(
                xaxis={
                    'title': xaxis_name.title(),
                    'type': 'linear' if xaxis_type == 'Linear' else 'log'
                    },
                yaxis={
                    'title': yaxis_name.title(),
                    'type': 'linear' if yaxis_type == 'Linear' else 'log'
                    },
                margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            )
        }

    # Caso esteja vazio
    else:
    
        return {
            
            'data': [go.Scatter(
                x=[ Loop for Loop in range(100) ],
                y=[ Loop ** 2 for Loop in range(100) ],
                #text=df['name'],
                mode='markers',
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'line': {'width': 0.5, 'color': 'white'}
                }
            )],

            'layout': go.Layout(
                xaxis={'title': 'Eixo X'},
                yaxis={'title': 'Eixo Y'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            )
        }

# Função para gerar PDF

# Callback para exportar o gráfico como um arquivo PDF quando o botão for clicado
@app.callback(
    Output('url', 'pathname'),
    [
        Input('xaxis', 'value'),
        Input('yaxis', 'value'),
        Input('xaxis-type', 'value'),
        Input('yaxis-type', 'value'),
        Input('year--slider', 'value'),
        Input('export-pdf-button', 'n_clicks'),
    ],
    prevent_initial_call=True
)
def export_pdf(xaxis_name, yaxis_name, xaxis_type, yaxis_type, year_value, n_clicks):
    
    # Cria um gráfico de dispersão de exemplo usando Plotly Express
    if n_clicks > 0:

        # Filtrar os dados
        Filtro = df[ df['anos'] == year_value]

        if xaxis_name and yaxis_name:

            fig = px.scatter( x=Filtro[xaxis_name], y=Filtro[yaxis_name], 
            labels={'x': xaxis_name.title(), 'y': yaxis_name.title()}, title=f'Análise {xaxis_name} x {yaxis_name} | {year_value}' )

            pdf_path = 'output.pdf'
            pio.write_image(fig, pdf_path, format='pdf', width=800, height=500)

            return f'/download/{pdf_path}'

    raise PreventUpdate

# Rota para fazer o download do arquivo PDF
@app.server.route('/download/<path:path>')
def download(path):
    return send_file(path, as_attachment=True)



if __name__ == '__main__':
    app.run_server( debug=True )