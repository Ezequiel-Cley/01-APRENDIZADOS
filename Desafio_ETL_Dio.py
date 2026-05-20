 # Importando Biblioteca
import pandas as pd
from google import genai

# Criando manualmente os dados dos clientes
users = [
    {'id': 1, 'name': 'Naruto', 'news': []},
    {'id': 2, 'name': 'Hinata', 'news': []},
    {'id': 3, 'name': 'Sakura', 'news': []},
    {'id': 4, 'name': 'Sasuke', 'news': []},
    {'id': 5, 'name': 'Kakashi', 'news': []},
]

# transformando os dados em um DataFrame
df_users = pd.DataFrame(users)

# Gerando função para conexão com Gemini e obtenção de informações
def gerar_conteudo_gemini(messages, api_key='GEMINI_API_KEY', model="gemini-3-flash-preview"):
  try:
          # Define o cliente para conectar com o Gemini
          client = genai.Client(api_key=api_key)
          
          # Chama o modelo para gerar as informações desejadas
          response = client.models.generate_content(
              model=model, 
              contents=messages
          )
          
          # Retorna a resposta em texto
          return response.text
          
  except Exception as e:
      print(f"Ocorreu um erro ao comunicar com o Gemini: {e}")
      return None

  # Obtendo as mensagens para cada usuário e armazenando no DataFrame
for user in df_users['name']:
  messages = f"""
    Você é um especialista em markting bancário.
      Crie uma mensagem para {user} sobre a importância dos investimentos (máximo de 100 caracteres)
  """
  news = gerar_conteudo_gemini(messages)
  print(news)
  df_users.loc[df_users['name'] == user, 'news'] = news

# Armazenando o DataFrame atualizado em um novo arquivo CSV
df_users.to_csv('Arquivo_atualizado.csv', sep=',', header=False)
