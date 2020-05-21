from pymongo import MongoClient

# Estabeleço a conexão client -> daemon/serviço
client = MongoClient()

# Defino a collection para trabalhar 
collection = client.pessoa # criei/carreguei 

for registro in collection.pessoa.find():
    print(registro)

for registro in collection.pessoa.find():
    print("-----------------")
    print('Nome:', registro['nome'])
    print('Empresa', registro['empresa'])
    print('Produto', registro['produto'])
    if registro.get('distros'):
        print('Distros', registro['distros'])
