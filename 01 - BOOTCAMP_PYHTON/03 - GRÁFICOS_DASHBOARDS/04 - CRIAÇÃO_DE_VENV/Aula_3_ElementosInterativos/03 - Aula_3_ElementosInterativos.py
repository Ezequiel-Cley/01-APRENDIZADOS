# framework Python usado para criar aplicativos web interativos com visualizações de dados.
import dash

import dash_core_components as dcc
# Esta biblioteca fornece os principais componentes interativos do Dash 
# dcc.Graph - Gráficos
# dcc.Dropdown - Um menu suspenso que permite aos usuários selecionar opções de uma lista.
# dcc.Slider -  controle deslizante que permite aos usuários selecionar um valor em um intervalo definido.

import dash_html_components as html
# Esta biblioteca fornece os componentes HTML básicos que você pode usar no layout do seu aplicativo Dash.
# html.Div: Um contêiner genérico que pode ser usado para agrupar outros componentes.
# html.H1, html.H2, ...: Tags de cabeçalho para títulos e subtítulos.
# html.P: Uma tag de parágrafo para texto.

# Instanciar o Dash
# cria uma instância da classe dash.Dash que é essencial para iniciar e configurar o aplicativo Dash.
app = dash.Dash()

app.layout = html.Div([

    ### ### ### 
    ### Graph  ###
    ### ### ###
    # Cria um gráfico
    html.Div([
        dcc.Graph(
        figure={
            'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Gráfico de Barras'}],
            'layout': {'title': 'Gráfico Interativo'}
        }
        ),
    ]),

    ### ### ### 
    ### Markdown  ###
    ### ### ###
    # Cria um gráfico
    html.Div([
        html.Br(),
        dcc.Markdown('**Texto em Negrito**')
    ]),

    ### ### ### 
    ### Link  ###
    ### ### ###
    # Para entrar em outra página
    html.Div([
        html.Br(),
        dcc.Link('Clique aqui para ir para outra página', href='/outra-pagina'),
    ]),

    ### ### ### 
    ### Tabs ###
    ### ### ###
    # Tabelas dinâmicas com abas
    html.Div([
        html.Br(),
        # dcc.Tabs e dcc.Tab
        dcc.Tabs([
            dcc.Tab(
                label='Tab 1', 
                children=[
                    html.Div('Conteúdo da Tab 1')
                ]
            ),
            dcc.Tab(
                label='Tab 2', 
                children=[
                    html.Div('Conteúdo da Tab 2')
                ]
            ),
        ]),
    ]),

    ### ### ### 
    ### Loading ###
    ### ### ###
    # Mostra informação sobre o carregamento
    html.Div([
        html.Br(),
        dcc.Loading(
            type='default', 
            children=[
                html.Div('Conteúdo que será exibido durante o carregamento...')
            ]
        ),
    ]),

    ### ### ### 
    ### ConfirmDialogProvider ###
    ### ### ###
    # Faz a confirmação com o usuário em tela
    html.Div([
        html.Br(),
        dcc.ConfirmDialogProvider(
            children=html.Button('Clique para ganhar 1 milhãoo'),
            id='confirm',
            message='Tem certeza que deseja continuar?'
        ),
    ]),   




])

# permite controlar o que será executado quando o script é iniciado diretamente.
if __name__ == '__main__':
    app.run_server( debug=True )