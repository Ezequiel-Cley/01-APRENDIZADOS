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

# Layout da aplicação | Frontend
# Dash usará esse layout para renderizar a interface do usuário do aplicativo. 
app.layout = html.Div([
    
    ### ### ### 
    ### DIV ###
    ### ### ###
    # Representa uma divisão genérica em um documento HTML
    
    ### ### ### 
    ### H1, H2, H3 ###
    ### ### ###
    # Cabeçalhos de diferentes níveis, usados para estruturar o conteúdo e definir hierarquias
    html.Div([
        html.H1('Div 1'),
        html.H2('Div 2'),
        html.H3('Div 3'),
    ]),

    ### ### ### 
    ### P ###
    ### ### ###
    # Parágrafo, usado para exibir texto normal
    html.Div([
        html.P('Este é um parágrafo de exemplo.'),
    ]),

    ### ### ### 
    ### Label ###
    ### ### ###
    # Rótulo associado a um elemento, como um campo de entrada
    html.Div([
        html.Label('Nome:'),
        html.Label('Idade:'),
        html.Label('Endereço:'),
    ]),

    ### ### ### 
    ### Span ###
    ### ### ###
    # Define um trecho de texto ou conteúdo inline com propriedades específicas
    html.Div([
        html.Span('Texto avulso na sua pagina'),
    ]),

    ### ### ### 
    ### Img ###
    ### ### ###
    # Exibe uma imagem
    html.Div([
        html.Img( src=app.get_asset_url('Icone.png'), height='150')
    ]),

    ### ### ### 
    ### A ###
    ### ### ###
    # Cria um link para outra página ou recurso
    html.Div([
        html.A('Acessar site do Google', href='https://www.google.com.br')
    ]),

    ### ### ### 
    ### Ul e Li ###
    ### ### ###
    # Lista não ordenada e itens da lista
    html.Div([
        html.Ul([
            html.Li('Item 1'),
            html.Li('Item 2'),
        ])
    ]),

    ### ### ### 
    ### Br ###
    ### ### ###
    # Cria uma quebra de linha
    html.Div([
        html.P('Paragráfo'),
        html.Br(),
        html.P('Pulou uma linha.')
    ]),

    ### ### ### 
    ### Em ###
    ### ### ###
    # Texto enfatizado, geralmente exibido em itálico
    html.Div([
        html.Em('enfatizado')
    ]),

    ### ### ### 
    ### Strong ###
    ### ### ###
    # Texto forte ou importante, geralmente exibido em negrito
    html.Div([
        html.Strong('importante')
    ]),

    ### ### ### 
    ### Pre  ###
    ### ### ###
    # Mantém a formatação do texto, exibindo-o em uma fonte de espaçamento fixo
    html.Div([
        html.Pre('    Manter o texto formatado.'),
        html.Label('    Manter o texto formatado.')
    ]),

    ### ### ### 
    ### Blockquote ###
    ### ### ###
    # Cria um bloco de citação em itálico.
    html.Div([
        html.Blockquote("Esta é uma citação interessante.")
    ]),

    ### ### ### 
    ### Code  ###
    ### ### ###
    # Formata um texto como código, geralmente exibido em uma fonte de espaçamento fixo.
    html.Div([
        html.Code("print('Hello, world!')")
    ]),

    ### ### ### 
    ### Button  ###
    ### ### ###
    # Cria um botão.
    html.Div([
        html.Button('Botão Padrão', id='button-default'),
    ]),

    ### ### ### 
    ### Tabela  ###
    ### ### ###
    # Cria uma tabela.
    html.Div([
        html.Table([
            html.Tr([html.Th('Nome'), html.Th('Idade')]),
            html.Tr([html.Td('Alice'), html.Td('25')]),
            html.Tr([html.Td('Bob'), html.Td('30')]),
            html.Tr([html.Td('Charlie'), html.Td('22')])
        ])
    ]),



])

# permite controlar o que será executado quando o script é iniciado diretamente.
if __name__ == '__main__':
    app.run_server( debug=True )