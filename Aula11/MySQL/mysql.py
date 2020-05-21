#1: import modulo para mysql
import pymysql
## import ou enviroments 

#2: conexao com o banco

try:
    conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='4linux', ### lembrar de ocultar informações sigilosas
                db='pessoa',
                charset='utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
              )
except Exception as err: ## verificar na documentação os erros para captura correta (boas práticas)    
            print('Erro ao conectar com o banco', err)

else:
    string_sql = """
    -- Passo2: Criar a tabela

    CREATE TABLE pessoa(
        id_pessoa int not null auto_increment,
        nome_pessoa varchar(50) not null,
        nacionalidade_pessoa varchar(20) not null,
        idade_pessoa int not null,
        PRIMARY KEY (id_pessoa)    
    );

    
    """
    
    with conexao.cursor() as cursor:
        cursor.execute(string_sql)
        conexao.commit()
        
        for registro in cursor:
            print(registro) #logica de manipulação...
   
    # fecha conexão
    conexao.close()                
