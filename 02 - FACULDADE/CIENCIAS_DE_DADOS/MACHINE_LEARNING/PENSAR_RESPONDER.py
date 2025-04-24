# Realizado importações
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# Realizando a leitura da base de Dados contendo os dados de vinhos para analise
df = pd.read_csv('wine_dataset.csv')
# Analisando a estrutura de Base dados que temos
df.head()

# Analisa base de dados
def Verificar_DataSet( Base_Dados ):

  # Verificando dimensão
  Dimensao = Base_Dados.shape
  print(f'Base de dados possui { Dimensao[0] } Linhas e {Dimensao[1] } Colunas')
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

# Chamando a função
Verificar_DataSet(df)

# Estatísticas básicas
df.describe().transpose()

# Estatísticas básicas - Categoricos
df.describe( include=['O'] ).transpose()

# Analisando Diferentes tipos de vilho!!!
df.groupby(['style']).sum()

# Converte a coluna 'Style' em valores numéricos e armazenando na coluna 'wine_type'
df['wine_type'] = df['style'].map({'red': 0, 'white': 1})
# Avaliando inclusão da coluna 'wine_type'
df.head()

# Realizado a Armazenamento dos Vinhos para ter como Recursos
y = df['style']
# Criando uma base sem os dados de 'style' para criar previsões como uma base de testes(Rótulos)
X = df.drop('style', axis=1).reset_index()

# Criando variaveis com os dados das Varaiveis X e Y para realizar o teste comparativo e ensinar como funciona os detalhes dos vinhos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando um Modelo para iniciar aprendizagem
modelo = GaussianNB()
# Definindo quais dados deve ser utilizado para realizar a aprendizagem.
modelo.fit(X_train, y_train)

# Definindo as bases para criar predição
y_pred = modelo.predict(X_test)
print("Acurácia:", y_pred)

# Realiza a Validação para identificar qual o % de compatibilidade(Acurácia)
accuracy = accuracy_score(y_test, y_pred)
print("Acurácia:", accuracy)

# Exibe o relatório de classificação
print(classification_report(y_test, y_pred))