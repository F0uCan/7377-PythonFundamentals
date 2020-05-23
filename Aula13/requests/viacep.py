
import requests 
import time

### enviar uma requisição http GET

destino = "https://viacep.com.br/ws/{}/json/" 

lista_cep = ['04101300', 
             '01310200', 
             '80530230', 
             '20271130',
             '40026280',
             '95670000',
             '66040170'
             ]
             
for cep in lista_cep:
    resposta = requests.get(destino.format(cep))
    
    if resposta.status_code == 200:
        json = resposta.json()
        print('------------------------')
        print('CEP: ', json['cep'])
        print('Logradouro: ', json['logradouro'])
        print('Bairro: ', json['bairro'])
        print('UF: ', json['uf'])
        print('IBGE: ', json['ibge'])
        print('GIA:' , json['gia'])
    else:
        print('Bad Request, no donut for you')
    
    time.sleep(1)
        
# armazenamento de dados csv, banco... 
### mercado financeiro
### mercados de bairro
###  



             
