import sqlite3

try:
    conexao = sqlite3.connect('data/pessoa.db')
except Exception as err: 
    print('Erro ao conectar com o banco de dados')
else:
    cursor = conexao.cursor()
    
    string_sql = """ SELECT * from pessoa  """
    
    cursor.execute(string_sql)
    
    #print(cursor.fetchall())
    for registro in cursor.fetchall():
        for campos in registro:
            print(campos)

### Converterem o exercício de filmes 
### ao invés de usar arquivos
### usem o banco sqlite

