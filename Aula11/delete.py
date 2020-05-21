from pymongo import MongoClient

# Estabeleço a conexão client -> daemon/serviço
client = MongoClient()

# Defino a collection para trabalhar 
collection = client.pessoa # criei/carreguei 

collection.pessoa.delete_one({'nome' : 'Tio Bill'})


#### 
