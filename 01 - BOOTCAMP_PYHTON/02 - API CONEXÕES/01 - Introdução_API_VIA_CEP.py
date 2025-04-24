#Exlipando o Uso de conexão atráves de API's

import requests

# Av Paulista - SP
Cep = '01001000'
Url = f'http://viacep.com.br/ws/{Cep}/json/'

# requests.get --> um método da biblioteca requests do Python, que é usada para enviar solicitações HTTP GET a um servidor web.
# Ele é usado para obter informações de uma determinada URL, como o conteúdo de uma página da web ou os dados de uma API.
Response = requests.get( Url )

# Avaliando o retorno
Response

type( Response )

# Acessando as informações no Json
Response.json()

# Transformo em dict
dict( Response.json() )

# Analisando as chaves
dict( Response.json() ).keys()

# Analisando os valores
dict( Response.json() ).values()

# Calculando tamanho dos elementos
len( dict( Response.json() ).keys() )

# Validar erros
if Response.status_code == 200:
  Dados = Response.json()
  print('Sucesso na consulta')

else:
  print('Erro de processamento')
  
# Mensagem de retorno
Response.reason

# Tempo da requisição
Response.elapsed

# codificação de caracteres usada na resposta
Response.encoding

# cabeçalhos da resposta HTTP da API
# Os cabeçalhos HTTP fornecem informações adicionais sobre a resposta da API
# como o tipo de conteúdo, a codificação usada, a data de modificação, etc.
Response.headers

# é um objeto urllib3.response.HTTPResponse que representa a resposta HTTP bruta retornada pela API.
# retorna a resposta HTTP na forma de bytes brutos, sem qualquer decodificação ou processamento adicional.
# Isso pode ser útil em situações em que precisamos manipular a resposta bruta antes de decodificá-la.
Response.raw


from pandas import DataFrame

# Função
def Buscar_Endereco( cep ):

  # Requisição
  Url = f' http://viacep.com.br/ws/{cep}/json/'
  Resposta = requests.get( Url )

  # Validando a resposta
  if Resposta.status_code == 200:
    Dados = Resposta.json()

    # Retorno
    return {
        'Cep' : Dados['cep'],
        'Logradouro' : Dados['logradouro'],
        'Bairro' : Dados['bairro'],
        'Cidade' : Dados['localidade'],
        'UF' : Dados['uf']
    }

  # Caseo de Erro
  else:
      print(f'Erro na solicatação da API: { Resposta.status_code } ')
	  
DataFrame( Buscar_Endereco('01001000'), index=[0] )
