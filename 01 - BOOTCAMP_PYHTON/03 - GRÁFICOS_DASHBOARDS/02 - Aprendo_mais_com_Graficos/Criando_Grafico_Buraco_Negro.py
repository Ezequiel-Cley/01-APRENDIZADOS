# Libs
import pandas as pd
import numpy as np

# plotly
import plotly.graph_objs as go
#import plotly.express as px

# Avisos
import warnings
warnings.filterwarnings('ignore')

# Configurar o número de casas decimais para 2
pd.options.display.float_format = '{:.2f}'.format

# Carregar os dados
Base_Dados_Ranking = pd.read_csv('timesData.csv')

# Verificar
Base_Dados_Ranking.head()


# Colunas
for Loop, Col in enumerate( Base_Dados_Ranking.columns ):
  print( Loop+1,'. ', Col)
  
  # Analisa base de dados
def Verificar_DataSet(Base_Dados ):

  # Verificando dimensão
  Dimensao = Base_Dados.shape
  print(f'Base de dados possui { Dimensao[0] } Linhas e {Dimensao[1] } Colunas')
  print('-' * 50 )

  # Tipo das Colunas
  Tipos_Colunas = Base_Dados.dtypes.value_counts()
  print(f'Tipo das colunas')
  print( pd.DataFrame( Tipos_Colunas, columns=['Quantidade_Colunas'] ) )
  print('-' * 50 )

  # Campos únicos
  Campos_Unicos = Base_Dados.nunique()
  print(f'Campos únicos')
  print( pd.DataFrame( Campos_Unicos, columns=['Quantidade_Campos'] ) )
  print('-' * 50 )

  # Campos nulos
  Campos_Nulus = Base_Dados.isnull().sum()
  print(f'Campos Nulos')
  print( pd.DataFrame( Campos_Nulus, columns=['Quantidade_Campos'] ) )
  print('-' * 50 )


Verificar_DataSet( Base_Dados_Ranking )

# Brasil nos ranks mundiais
Base_Dados_Ranking[  Base_Dados_Ranking.country =='Brazil' ].university_name.unique()

# Ano
Base_Dados_Ranking['year'].value_counts().sort_index()

# Analise
Anl_1 = Base_Dados_Ranking[ Base_Dados_Ranking['year'] == 2016 ].sort_values( by=['teaching', 'citations'], ascending=False ).head(10)

Anl_1.shape

# Criar uma figura
Figura_01 = go.Figure()

type( Figura_01 )

# Gráfico Linhas

# Criar uma figura
Figura_01 = go.Figure()

# Grafico 1
Figura_01.add_trace(

  # instanciar o gráfico
  go.Scatter(
      # Eixo x
      x = Anl_1.university_name,
      # Eixo y
      y = Anl_1.citations,
      # Modo do gráfico
      mode = 'lines',
      # Nome
      name = 'citations',
      # Marcadores
      marker = dict( color='rgba(16, 112, 2, 0.8)' ),
      # Label
      text = Anl_1.university_name
  )
)

# Grafico 2
Figura_01.add_trace(

  # instanciar o gráfico
  go.Scatter(
      # Eixo x
      x = Anl_1.university_name,
      # Eixo y
      y = Anl_1.teaching,
      # Modo do gráfico
      mode = 'lines+markers',
      # Nome
      name = 'teaching',
      # Marcadores
      marker = dict( color='rgba(80, 26, 80, 0.8)' ),
      # Label
      text = Anl_1.university_name
  )
)

# Ajuste de layout
Figura_01.update_layout(
    # Titulo
    title='Scoore de Citação e Ensino | Top 10 universidade globais',
    xaxis = dict(
        # Title
        title = 'Ranking Mundial',
        zeroline = False
    )
)


Figura_01.show()

# Scater
Anl_2 = Base_Dados_Ranking[ Base_Dados_Ranking['year'] == 2016 ]

# Figura
Figura_02 = go.Figure()

# Gráfico
Figura_02.add_trace(
    go.Scatter(
        x=Anl_2.teaching,
        y=Anl_2.citations,
        mode='markers',
        text=Anl_2.university_name,
        marker=dict( size=10 ),
        marker_color='rgba(0, 60, 255, 0.3)',
        marker_line_width=1
    )
)

# Gráfico
Figura_02.update_layout(
    title='Análise teaching x citations global | 2016',
    xaxis=dict( title='teaching', ticklen=5, zeroline=False ),
    yaxis=dict( title='citations', ticklen=5, zeroline=False )
)

Figura_02.show()

# Analise
Analise_Rank_Pais = Base_Dados_Ranking.groupby( by=['country', 'year'] ).agg(
    Media_Aprendizado = ('teaching', 'mean'),
    Mediana_Aprendizado = ('teaching', 'median'),
    Media_Citacoes = ('citations', 'mean'),
    Mediana_Citacoes = ('citations', 'median'),
    Quantidade = ('year', 'count')
).reset_index()

# Veriricando
Analise_Rank_Pais.head(10)

# Figura
Figura_03 = go.Figure()

# Filtro
Anl_3 = Analise_Rank_Pais[ Analise_Rank_Pais.year == 2016 ].sort_values( by='Quantidade', ascending=False ).head(10)

# evento
'''
Anl_3_A = Anl_3
Anl_3_A['Soma_Score'] = Anl_3.Media_Citacoes + Anl_3.Media_Aprendizado
Anl_3_A.sort_values( by=['Soma_Score'], ascending=False )
'''

# Grafico 1
Figura_03.add_trace(
    go.Bar(
        x=Anl_3.country,
        y=Anl_3.Media_Aprendizado,
        name='teaching',
        marker=dict(
            color='rgba(255, 174, 255, 0.5)',
            line=dict(color='rgb(0, 0 ,0)', width=1.5)
        )
    )
)

# Grafico 2
Figura_03.add_trace(
    go.Bar(
        x=Anl_3.country,
        y=Anl_3.Media_Citacoes,
        name='citations',
        marker=dict(
            color='rgba(255, 255, 128, 0.5)',
            line=dict(color='rgb(0, 0 ,0)', width=1.5)
        )
    )
)

# Ajuste no Latour
Figura_03.update_layout(
  title = 'Análise Países com maiores avaliasões | Ano 2016',
)

Figura_03.show()

Analise_Rank_Pais[ (Analise_Rank_Pais.year == 2016) & ( Analise_Rank_Pais.country == 'Brazil') ].sort_values( by='Quantidade', ascending=False )

Anl_3.head()

# Gráfico de Pizza / Rosca

# Figura
Figura_04 = go.Figure()

# Grafico
Figura_04.add_trace(
    go.Pie(
        labels=Anl_3.country,
        values=Anl_3.Quantidade,
        pull=0.01,
        hole=.4,
        hoverinfo='label+percent+value'
    )
)

# Ajuste de Laoyout
Figura_04.update_layout(
    title_text = 'Quantidade de universidades por país',
    annotations = [
        dict( text=f'{ Anl_3.Quantidade.sum() }',
             x=0.5, y=0.5,
              font_size=20,
              showarrow=False )
    ]
)

Figura_04.show()

Anl_3.columns

# Bolhas
go.Figure(
    data=[
        go.Scatter(
            x=Anl_3.Media_Aprendizado,
            y=Anl_3.Media_Citacoes,
            mode='markers',
            marker=dict(
                size=Anl_3.Quantidade ** 1.5,
                sizemode='area'
            )
        )
    ]
)

Base_Dados_Ranking.head(2)

# Histograma
Figura_05 = go.Figure()

Figura_05.add_trace(
    go.Histogram(
        x=Base_Dados_Ranking[ Base_Dados_Ranking.year == 2011 ].teaching,
        opacity=0.75,
        name = '2011',
        marker= dict( color='rgba(171, 50, 96, 0.6)')
    )
)

Figura_05.add_trace(
    go.Histogram(
        x=Base_Dados_Ranking[ Base_Dados_Ranking.year == 2012 ].teaching,
        opacity=0.75,
        name = '2012',
        marker= dict( color='rgba(12, 50, 196, 0.6)')
    )
)


Figura_05.add_trace(
    go.Histogram(
        x=Base_Dados_Ranking[ Base_Dados_Ranking.year == 2013 ].teaching,
        opacity=0.75,
        name = '2013',
        marker= dict( color='rgba(14, 99, 37, 0.6)')
    )
)

Figura_05.update_layout(
  barmode='overlay',
  xaxis=dict(title='teaching'),
  yaxis=dict( title='Count'),
)

Figura_05.show()

# Boxplot
go.Figure(
    data=[
        go.Box(
            x=Base_Dados_Ranking.country,
            y=Base_Dados_Ranking.teaching
        )
    ]
)

# Criação dos dados para o gráfico
theta = np.linspace(0, 2*np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

r = 1.5  # Raio do buraco negro
x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

# Criação do disco de acreção
disk_radius = 2.5  # Raio do disco de acreção
disk_height = 0.1  # Espessura do disco de acreção
x_disk = disk_radius * np.cos(theta)
y_disk = disk_radius * np.sin(theta)
z_disk = np.ones_like(x_disk) * (r + disk_height)

# Criação do disco translúcido de acreção
disk_transparency = 0.7  # Transparência do disco de acreção
fig = go.Figure()

# Adição do disco translúcido ao gráfico
fig.add_trace(go.Mesh3d(
    x=x_disk.flatten(),
    y=y_disk.flatten(),
    z=z_disk.flatten(),
    alphahull=0,
    opacity=disk_transparency,
    color='grey'
))

# Criação do gráfico de superfície (buraco negro)
fig.add_trace(go.Surface(z=z, x=x, y=y, colorscale='Greys'))

# Definição das linhas curvas para representar a distorção do espaço
scale = 2.0
x_lines_centered = scale * np.sin(phi) * np.cos(theta)
y_lines_centered = scale * np.sin(phi) * np.sin(theta)
z_lines_centered = scale * np.cos(phi)

# Adição das linhas curvas ao gráfico
fig.add_trace(go.Scatter3d(
    x=x_lines_centered.flatten(),
    y=y_lines_centered.flatten(),
    z=z_lines_centered.flatten(),
    mode='lines',
    line=dict(color='red', width=3),
    hoverinfo='none'
))

# Adição da seta representando o horizonte de eventos
horizon_event_arrow_scale = 0.5
fig.add_trace(go.Cone(
    x=[0],
    y=[0],
    z=[r],
    u=[0],
    v=[0],
    w=[-horizon_event_arrow_scale],
    showscale=False,
    sizemode="absolute",
    sizeref=1,
    anchor="tip",
    colorscale='Greys',
    opacity=0.7
))

# Personalização do layout do gráfico para ocupar 100% do espaço da tela
fig.update_layout(
    title='Simulação Artisitca de um Buraco Negro usando Plotly',
    scene=dict(
        xaxis_title='Eixo X',
        yaxis_title='Eixo Y',
        zaxis_title='Eixo Z',
    ),
    width=None,
    height=800,
)

# Exibição do gráfico
fig.show()

# Criação dos dados para o gráfico
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)
r = 1.5  # Raio do buraco negro
x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

# Criação do disco de acreção
disk_radius = 2.5  # Raio do disco de acreção
disk_height = 0.1  # Espessura do disco de acreção
x_disk = disk_radius * np.cos(theta)
y_disk = disk_radius * np.sin(theta)
z_disk = np.ones_like(x_disk) * (r + disk_height)

# Criação das coordenadas das 4 esferas menores em volta do buraco negro
small_sphere_radius = 0.2
small_sphere_distance = 2.0
x_spheres = [
    r + small_sphere_distance * np.cos(np.pi / 4),
    r + small_sphere_distance * np.cos(3 * np.pi / 4),
    r + small_sphere_distance * np.cos(5 * np.pi / 4),
    r + small_sphere_distance * np.cos(7 * np.pi / 4)
]
y_spheres = [
    small_sphere_distance * np.sin(np.pi / 4),
    small_sphere_distance * np.sin(3 * np.pi / 4),
    small_sphere_distance * np.sin(5 * np.pi / 4),
    small_sphere_distance * np.sin(7 * np.pi / 4)
]
z_spheres = np.ones_like(x_spheres) * small_sphere_radius

# Criação do disco translúcido de acreção
disk_transparency = 0.7  # Transparência do disco de acreção
fig = go.Figure()

# Adição do disco translúcido ao gráfico
fig.add_trace(go.Mesh3d(
    x=x_disk.flatten(),
    y=y_disk.flatten(),
    z=z_disk.flatten(),
    alphahull=0,
    opacity=disk_transparency,
    color='grey'
))

# Criação do gráfico de superfície (buraco negro)
fig.add_trace(go.Surface(z=z, x=x, y=y, colorscale='Greys'))

# Definição das linhas curvas para representar a distorção do espaço
scale = 2.0
x_lines_centered = scale * np.sin(phi) * np.cos(theta)
y_lines_centered = scale * np.sin(phi) * np.sin(theta)
z_lines_centered = scale * np.cos(phi)

# Adição das linhas curvas ao gráfico
fig.add_trace(go.Scatter3d(
    x=x_lines_centered.flatten(),
    y=y_lines_centered.flatten(),
    z=z_lines_centered.flatten(),
    mode='lines',
    line=dict(color='red', width=3),
    hoverinfo='none'
))

# Adição das 4 esferas menores ao gráfico
spheres_trace = go.Scatter3d(
    x=x_spheres,
    y=y_spheres,
    z=z_spheres,
    mode='markers',
    marker=dict(size=10, color='blue'),
    hoverinfo='none'
)
fig.add_trace(spheres_trace)

# Adição da seta representando o horizonte de eventos
horizon_event_arrow_scale = 0.5
fig.add_trace(go.Cone(
    x=[0],
    y=[0],
    z=[r],
    u=[0],
    v=[0],
    w=[-horizon_event_arrow_scale],
    showscale=False,
    sizemode="absolute",
    sizeref=1,
    anchor="tip",
    colorscale='Greys',
    opacity=0.7
))

# Configuração da animação
frames = []
for t in np.linspace(0, 2 * np.pi, 100):
    frame_data = go.Scatter3d(
        x=[x_spheres[i] for i in range(4)],
        y=[y_spheres[i] * np.cos(t) - z_spheres[i] * np.sin(t) for i in range(4)],
        z=[y_spheres[i] * np.sin(t) + z_spheres[i] * np.cos(t) for i in range(4)],
        mode='markers',
        marker=dict(size=10, color='blue'),
        hoverinfo='none',
        text=[f'Orbita {i+1}' for i in range(4)]  # Texto das bolinhas na animação
    )
    frame = go.Frame(data=[frame_data], name=f'frame_{t:.2f}')
    frames.append(frame)

# Adição dos frames à animação
fig.update(frames=frames)
updatemenus = [dict(type='buttons', showactive=False, buttons=[dict(label='Play', method='animate', args=[None, dict(frame=dict(duration=50, redraw=True), fromcurrent=True, mode='immediate')]), dict(label='Pause', method='animate', args=[[None], dict(frame=dict(duration=0, redraw=False), mode='immediate')])], x=0.1, y=0, xanchor='right', yanchor='bottom')]
sliders = [dict(steps=[dict(args=[f'frame_{t:.2f}', dict(mode='immediate')], label=f'{t:.2f}', method='animate') for t in np.linspace(0, 2 * np.pi, 100)], active=0, currentvalue=dict(prefix='Tempo: ', visible=True), pad=dict(t=50), x=0, y=0, len=0.9)]

# Personalização do layout do gráfico para ocupar 100% do espaço da tela
fig.update_layout(
    title='Simulação de um Buraco Negro com Disco de Acreção e Horizonte de Eventos',
    scene=dict(
        xaxis_title='Eixo X',
        yaxis_title='Eixo Y',
        zaxis_title='Eixo Z',
        aspectratio=dict(x=1, y=1, z=1),
        camera=dict(up=dict(x=0, y=0, z=1), eye=dict(x=-1.25, y=1.25, z=1.25)),
    ),
    width=None,
    height=800,
    updatemenus=updatemenus,
    sliders=sliders,
)

# Exibição do gráfico
fig.show()