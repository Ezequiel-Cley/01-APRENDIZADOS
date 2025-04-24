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
    ### Customização ###
    ### ### ###
    # Layout de uma Div
    html.Div([

        html.Div( 
            'Configurando padrões de estilo da Fonte',

            style={

                # Define a cor do texto
                'color': '#126527', 

                # Define o tamanho da fonte
                'font-size': '30px',

                # Define a família da fonte
                'font-family': 'Arial, sans-serif',

                # Define a espessura da fonte (normal, bold, bolder, lighter, 100-900).
                'font-weight': 'bold',

                # Define o estilo da fonte (normal, italic, oblique).
                'font-style': 'italic',

                # Alinha o texto horizontalmente (left, right, center, justify).
                'text-align': 'center',

                # Define a altura da linha
                'line-height': '3.5',

                # Define o espaçamento entre caracteres
                'letter-spacing': '5px',

                # Transforma o texto (capitalize, uppercase, lowercase).
                'text-transform': 'uppercase'
            }
        )
    ]),

    html.Div(
        'Outro Texto',

        style={
            # Define a cor de fundo da Div.
            'background-color': 'lightgray',

            # Define a largura
            'width': '300px',

            # Define a altura
            'height': '150px',

            # Define o preenchimento interno
            'padding': '10px',

            # Define a margem externa
            'margin': '10px',

            # Define a borda da .
            'border': '2px solid gray',

            # Define o raio da borda arredondada
            'border-radius': '10px',

            # Adiciona uma somb ra à Div.
            'box-shadow': '2px 2px 5px gray',

            # Controla como a Div é exibida (block, inline, inline-block).
            'display': 'inline',

            # Define o alinhamento flutuante (left, right).
            'float': 'right',
        }
    )




])

# permite controlar o que será executado quando o script é iniciado diretamente.
if __name__ == '__main__':
    app.run_server( debug=True )