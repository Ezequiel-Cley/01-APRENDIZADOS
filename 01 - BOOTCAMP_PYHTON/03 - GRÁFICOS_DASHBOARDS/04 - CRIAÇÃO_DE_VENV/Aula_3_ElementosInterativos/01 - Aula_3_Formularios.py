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
    ### Input  ###
    ### ### ###
    # Cria um campo de entrada de texto
    html.Div([
        dcc.Input(type='text', placeholder='Digite algo...'),
        html.Br(),
        html.Div(id='output-div')
    ]),

    ### ### ### 
    ### Textarea ###
    ### ### ###
    # Cria um campo de entrada de texto
    html.Div([
        html.Br(),
        dcc.Textarea(
            value='Digite seu texto aqui...',
        )
    ]),

    ### ### ### 
    ### Checklist ###
    ### ### ###
    # Cria uma lista de caixas de seleção
    html.Div([
        html.Br(),
        dcc.Checklist(
            options=[
                {'label': 'Opção 1', 'value': 'opcao1'},
                {'label': 'Opção 2', 'value': 'opcao2'}
            ],
            value=['opcao1']
        )
    ]),

    ### ### ### 
    ### RadioItems ###
    ### ### ###
    # Cria um grupo de botões de rádio
    html.Div([
        html.Br(),
        dcc.RadioItems(
            options=[
                {'label': 'Opção A', 'value': 'opcaoA'},
                {'label': 'Opção B', 'value': 'opcaoB'}
            ],
            value='opcaoA'
        )
    ]),

    ### ### ### 
    ### Dropdown ###
    ### ### ###
    # Cria um menu suspenso de seleção única
    html.Div([
        html.Br(),
        dcc.Dropdown(
            options=[
                {'label': 'Opção X', 'value': 'opcaoX'},
                {'label': 'Opção Y', 'value': 'opcaoY'}
            ],
            value='opcaoX'
        )
    ]),

    ### ### ### 
    ### Slider ###
    ### ### ###
    # Cria um controle deslizante para seleção numérica.
    html.Div([
        html.Br(),
        dcc.Slider(
            min=0,
            max=10,
            step=1,
            value=5
        )
    ]),

    ### ### ### 
    ### DatePickerSingle ###
    ### ### ###
    # Cria um seletor de data.
    html.Div([
        html.Br(),
        dcc.DatePickerSingle(
            date='2023-08-09'
        )
    ]),

    ### ### ### 
    ### DatePickerRange  ###
    ### ### ###
    # Cria um seletor de intervalo de datas.
    html.Div([
        html.Br(),
        dcc.DatePickerRange(
        start_date='2023-08-01',
        end_date='2023-08-31'
        )
    ]),

    ### ### ### 
    ### Upload ###
    ### ### ###
    # Cria um componente de upload de arquivos.
    html.Div([
        html.Br(),
        dcc.Upload(
        id='upload-data',
        children=html.Button('Upload de Arquivo'),
        multiple=True
    )
    ]),

    ### ### ### 
    ### RangeSlider ###
    ### ### ###
    # Cria um controle deslizante para seleção de intervalo numérico.
    html.Div([
        html.Br(),
        dcc.RangeSlider(
            marks={i: str(i) for i in range(0, 11)},
            min=0,
            max=10,
            step=1,
            value=[3, 7]
        )
    ]),



])

# permite controlar o que será executado quando o script é iniciado diretamente.
if __name__ == '__main__':
    app.run_server( debug=True )