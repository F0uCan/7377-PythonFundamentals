# from montydb import MontyClient
from pymongo import MongoClient

client = MongoClient()
# client = MontyClient('data/pessoa') 
## mock 

### hostname = ip/endereço
### porta 
### usuario, senha
#### mongourl 


collection = client.pessoa # criei/carreguei 

lista = [{
            'nome': 'John Maddog Hall',
            'empresa': 'Bazaar',
            'produto': 'Open Software Foundation'
 
         },
        
         {
            'nome': 'Steve Jobs',
            'empresa': 'Apple',
            'produto': 'mac OSX'
        
         }
        ]

## INSERT 

for item in lista:
    collection.pessoa.insert_one(item)
    

## SELECT (consulta)

## Update

## DELETE
