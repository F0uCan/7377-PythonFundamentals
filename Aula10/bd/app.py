### sqlite 


### DriverConexão ; interpretador do python conversar com o SGBD
import sqlite3

try:
    conexao = sqlite3.connect('data/pessoa.db')
except Exception as err: 
    print('Erro ao conectar com o banco de dados')
else:
    cursor = conexao.cursor()
    
    nome = "Joana"
    sobrenome = "Zanelato"
    cpf = 211111
    idade = 30
    estado = 'SP'
    
    sql_string = f"""
        insert into pessoa(cpf,nome,sobrenome,idade,estado)
        values({cpf},"{nome}","{sobrenome}",{idade},"{estado}");
    """
    
    cursor.execute(sql_string)
    
    conexao.commit()
    
    conexao.close()
    
    
    
    
      
