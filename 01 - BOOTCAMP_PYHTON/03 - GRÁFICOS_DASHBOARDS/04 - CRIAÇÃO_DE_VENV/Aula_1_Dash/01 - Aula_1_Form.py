# framework Python usado para criar aplicativos web interativos com visualizações de dados.
import dash

# Esta biblioteca fornece os principais componentes interativos do Dash 
# dcc.Graph - Gráficos
# dcc.Dropdown - Um menu suspenso que permite aos usuários selecionar opções de uma lista.
# dcc.Slider -  controle deslizante que permite aos usuários selecionar um valor em um intervalo definido.
import dash_core_components as dcc

# Esta biblioteca fornece os componentes HTML básicos que você pode usar no layout do seu aplicativo Dash.
# html.Div: Um contêiner genérico que pode ser usado para agrupar outros componentes.
# html.H1, html.H2, ...: Tags de cabeçalho para títulos e subtítulos.
# html.P: Uma tag de parágrafo para texto.
import dash_html_components as html

# Classes Input e Output do módulo dash.dependencies. 
# Essas classes são usadas em conjunto com o @app.callback 
# para definir as entradas e saídas de uma função de callback no Dash.
from dash.dependencies import Input, Output

# Instanciar o Dash
# cria uma instância da classe dash.Dash que é essencial para iniciar e configurar o aplicativo Dash.
app = dash.Dash()

# Layout da aplicação | Frontend
#  Dash usará esse layout para renderizar a interface do usuário do aplicativo. 
app.layout = html.Div([
    
    html.H1('Cadastro de usuário'),

    html.Label('Nome:'),
    dcc.Input( id='input-name', type='text', placeholder='Digite seu nome'),

    html.Label('Idade:'),
    dcc.Input(id='input-age', type='number', placeholder='Digite sua idade'),

    html.Label('Salário:'),
    dcc.Input(id='input-salary', type='number', placeholder='Digite seu salário'),

    html.Br(),
    html.Div(id='output-data')

])

# Ele é usado para definir a lógica que conecta os componentes interativos do frontend com as saídas e atualizações no backend.
# Usa o decorador @app.callback para vincular uma função Python a uma ou mais saídas e gatilhos (inputs) específicos. Essa função será executada sempre que os valores dos inputs especificados forem alterados.

# Output('nome_da_saida', 'propriedade_da_saida'): Especifica a saída que será atualizada e a propriedade dessa saída que será modificada quando a função 
# [Input('nome_do_gatilho', 'propriedade_do_gatilho')]: Especifica o(s) input(s) que a função monitorará para decidir quando executar a atualização da saída. Se qualquer um desses inputs tiver seu valor alterado, a função atualizar_saida será acionada.


# Callback para atualizar a saída com as informações do formulário | Backend
@app.callback(

    # Saida da minha função | A propriedade children é usada para renderizar texto ou componentes dentro do componente especificado.

    # No Dash, a propriedade children é um conceito fundamental 
    # que é usada para renderizar conteúdo dentro de um componente. 
    # Ela permite que você coloque texto ou outros componentes como filhos (children) do componente pai. 
    # Isso é essencial para criar layouts flexíveis e dinâmicos em um aplicativo Dash.
    Output('output-data', 'children'),

    # Entrada dos dados
    [Input('input-name', 'value'),
     Input('input-age', 'value'),
     Input('input-salary', 'value')]

)
def update_output(name, age, salary):
    
    # se os 3 campos foram preenchidos
    if name and age and salary:

        Div_saida = html.Div([
            html.H3(f'Informações fornecidas:'),
            html.P(f'Nome: {name}'),
            html.P(f'Idade: {age}'),
            html.P(f'Salário: R${salary:.2f}')
        ])

        return Div_saida

    else:
        return html.Div('Preencha todos os campos.')

# Criar a aplicação
#  o código if __name__ == '__main__': 
# garante que a execução do servidor só aconteça quando o script for executado diretamente como um programa principal, 
# e não quando ele é importado como um módulo em outro script. 


# Isso permite que você tenha controle sobre a execução do aplicativo Dash e _
# evita que ele seja executado acidentalmente ao importá-lo em outros scripts.

# permite controlar o que será executado quando o script é iniciado diretamente.
if __name__ == '__main__':
    app.run_server( debug=True )