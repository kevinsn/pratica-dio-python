import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/01001000/json/'.format(cep))
    # print(response.status_code)
    # print(response.text)
    print(response.json())
    print(type(response.text))
    print(type(response.json()))
    dados_cep = response.json()
    # print(dados_cep['logradouro'])
    # print(dados_cep['complemento'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    # retorna_dados_cep('01001000')
    # print(retorna_dados_pokemon('incineroar'))
    response = retorna_response('https://www.google.com.br')
    print(response)