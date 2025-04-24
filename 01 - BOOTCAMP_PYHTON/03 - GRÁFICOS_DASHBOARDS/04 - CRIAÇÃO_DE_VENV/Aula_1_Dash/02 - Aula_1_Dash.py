import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('timesData.csv')
print( df.head() )

# Instanciar o Dash
app = dash.Dash()

# Construindo as opções de Ano
Opcoes_Ano = []
for Ano in df['year'].unique():
    Opcoes_Ano.append( {'label':str(Ano),'value':Ano} )

# Layout
app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown( id='year-picker', options=Opcoes_Ano, value=df['year'].min() )
])

# Backend
@app.callback(
    Output('graph', 'figure'),
    [Input('year-picker', 'value')]
)
def update_figure(Ano_Selecao):
    
    # Filtro minha base de dados
    Filtro = df[df['year'] == Ano_Selecao].head(10)

    traces = []
    for Universidade in Filtro['university_name'].unique():

        df_universidade = Filtro[Filtro['university_name'] == Universidade]

        traces.append(
            go.Scatter(
                x=df_universidade['teaching'],
                y=df_universidade['citations'],
                text=df_universidade['university_name'],
                mode='markers',
                opacity=0.7,
                marker={'size': 15},
                name=Universidade
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'Aprendizagem'},
            yaxis={'title': 'Citações'},
            hovermode='closest'
        )
    }


# Criar a aplicação
if __name__ == '__main__':
    app.run_server( debug=True )