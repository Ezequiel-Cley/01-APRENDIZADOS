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

    # Parte 1: Div superior com o título
    html.Div(
        'Aula de Frontend com Dash',
        style={
            'font-size': '24px',
            'text-align': 'center',
            'padding': '10px'
        }
    ),

    # Parte 2: Div com 4 divs internas
    html.Div([
        html.Div('Indicador 1', style={'background-color': 'lightblue', 'height': '200px','width':'20%', 'margin':'15px', 'border-radius':'20px'}),
        html.Div('Indicador 2', style={'background-color': 'lightgreen', 'height': '200px','width':'20%', 'margin':'15px', 'border-radius':'20px'}),
        html.Div('Indicador 3', style={'background-color': 'lightcoral', 'height': '200px','width':'20%', 'margin':'15px', 'border-radius':'20px'}),
        html.Div('Indicador 4', style={'background-color': 'lightpink', 'height': '200px','width':'20%', 'margin':'15px', 'border-radius':'20px'}),
    ], style={'height': '400px', 'width': '100%', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}),

    # Parte 3: Div com 2 divs internas de 50% de largura
    html.Div([
        html.Div('Div Esquerda', style={'background-color': 'lightblue', 'height': '600px', 'width': '50%', 'float': 'left'}),
        html.Div('Div Direita', style={'background-color': 'lightgreen', 'height': '600px', 'width': '50%', 'float': 'right'}),
    ], style={'width': '100%', 'display': 'block'}),

    # Parte 4: Rodapé
    html.Div(
        'Rodapé #Dashboard com Python',
        style={
            'position': 'fixed',
            'bottom': '0',
            'width': '100%',
            'background-color': 'lightgray',
            'text-align': 'center',
            'padding': '10px'
        }
    )


])

# permite controlar o que será executado quando o script é iniciado diretamente.
if __name__ == '__main__':
    app.run_server( debug=True )