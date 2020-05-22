# Criação de Tabelas

cria_tabela_usuario = """
   CREATE TABLE usuario(
      id int not null primary key auto_increment,
      nome VARCHAR(50) not null,
      sobrenome VARCHAR(50) not null,
      login VARCHAR(20) not null,
      senha VARCHAR(20) not null, 
      reset boolean not null,
      admin boolean not null,
      tentativas int not null
   
   ) ;


"""

insert_admin = """
    INSERT INTO usuario(nome, sobrenome,login,senha,reset,admin,tentativas)
    VALUES ("root", "root", "root", "4linux",0,0,0);   

"""


query_entrar = """
    SELECT login, senha from usuario
    where login = {}

"""
