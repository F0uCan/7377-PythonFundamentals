# imports 

import requests 

### enviar uma requisição http GET

destino = "https://viacep.com.br/ws/{}/json/" 
cep = "04101300"

resposta = requests.get(destino.format(cep))

### status code 

if resposta.status_code == 200:
    json = resposta.json()
    print('CEP: ', json['cep'])
    print('Logradouro: ', json['logradouro'])
    print('Bairro: ', json['bairro'])
    print('UF: ', json['uf'])
    print('IBGE: ', json['ibge'])
    print('GIA:' , json['gia'])
    
    
else:
    print("erro")
    
    
