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

cria_tabela_conta =   """
    CREATE TABLE conta(
        id int not null primary key auto_increment,
        id_usuario int not null,
        agencia int not null,
        conta int not null,
        saldo float not null,
        foreign key (id_usuario) references usuario(id)
    );
    
"""

cria_tabela_movimentacao = """
    CREATE table movimentacao(
        id int not null primary key auto_increment,
        conta_origem int not null,
        conta_destino int not null,
        tipo_transacao varchar(20) not null,
        valor float not null
        );


"""



insert_admin = """
    INSERT INTO usuario(nome, sobrenome,login,senha,reset,admin,tentativas)
    VALUES ("root", "root", "root", "4linux",0,0,0);   

"""

insert_cliente = """
    INSERT INTO usuario(nome, sobrenome, login, senha, reset, admin,tentativas)
    VALUES("{}","{}","{}","{}", {}, {}, {}) 

"""

query_entrar = """
    SELECT id, login, senha, admin from usuario
    where login = "{}"

"""
query_consultaUsuario = """

    SELECT login from usuario
    where login = "{}" 
    
    
"""

query_update_reset = """
    UPDATE usuario
    SET senha = "{}"
    where login = "{}"
""" 

query_desbloqueia_usuario = """
    UPDATE usuario
    SET tentativas = 0
    where login = "{}"

"""
query_cadConta  = """
INSERT INTO conta(id_usuario, agencia, conta, saldo)
VALUES ({},{},{},{});


"""

## deixar as queries que serão utilizadas no programa
