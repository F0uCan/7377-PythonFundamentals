from pymongo import MongoClient
# import/ acesso variaveis de ambiente
# Estabeleço a conexão client -> daemon/serviço

try:
    client = MongoClient()
except Exception as err:
    print('erro ao conectar com o banco de dados', err)
else:
    # Defino a collection para trabalhar 
    collection = client.pessoa # criei/carreguei 
    
    
    collection.pessoa.update_one({'nome': 'Bill Gates'},
                                 {'$set': {'produto':'Windows', 'nome': 'Tio Bill'}})
                                     
    
