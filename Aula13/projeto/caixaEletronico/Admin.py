from .BD import ConexaoBanco
from .SQL.query import *
from random import randint
        
class Admin:
    def __init__(self):
        self.nome =''
        self.sobrenome =''
        self.email =''
        self.login = ''
        self.password = ''
        self.reset = 1
        self.tentativas = 0
        self.admin = True
        self.bd = ConexaoBanco()
        
        
    def cadUsuario(self):
        ## Captura as informações para criação de usuário
        print("Cadastro de Cliente")
        
        self.nome = input('Nome: ')
        self.sobrenome = input('Sobrenome: ')
        self.login = input('login: ')
        self.password = self.gerarSenhaTemp() 
        self.reset = 1
        self.tentativas = 0
        self.admin = 0

        ## Inicia conexão com o banco de dados
        try:
            self.bd.iniciaConexao()
        except Exception as err:
            print("Erro ao conectar com o Banco de dados")
        else:
            self.bd.executaSQL(insert_cliente.format(
                self.nome,
                self.sobrenome,
                self.login,
                self.password,
                self.reset,
                self.admin,
                self.tentativas,
                )
            )
            
            
            self.bd.terminaConexao()
        
    def resetSenha(self):
        ## Captura informação de acordo com ID
        print("Resetar Senha")
        self.login = input("Informe o login: ")
        
        ## Valida se o login existe no banco..
        
        self.bd.iniciaConexao()
        
        for registro in self.bd.executaSQL(query_consultaUsuario.format(self.login)):
            if self.login == registro['login']:
                self.bd.executaSQL(query_update_reset.format(
                    self.gerarSenhaTemp(),
                    self.login))
                print("Senha reiniciada com sucesso")
                break
        else:
            print("Login não encontrado") 
        
    def desbloquearUsuario(self):
        print("Desbloquear Usuário")
        self.login = input("Informe o login: ")
        
        ## Valida se o login existe no banco..
        self.bd.iniciaConexao()
        
        for registro in self.bd.executaSQL(query_consultaUsuario.format(self.login)):
            if self.login == registro['login']:
                self.bd.executaSQL(query_desbloqueia_usuario.format(self.login))
                print("Usuário Desbloqueado com sucesso")
                break
        else:
            print("Login não encontrado") 
        
        
    def gerarSenhaTemp(self):
        senha = ""
        for i in range(8):
            senha += str(chr(randint(60,90)))
        return senha
        
    def cadConta(self):
        print("Cadastro de conta")
        
        id_usuario = input("ID: ")
        agencia = input("Agência: ")
        conta = input("Conta: ")
        saldo = input("Saldo Inicial: ")
        
        try:
            self.bd.iniciaConexao()
        except Exception as err:
            print("Erro ao conectar com o Banco de dados")
        else:
            self.bd.executaSQL(query_cadConta.format(
                id_usuario,
                agencia,
                conta,
                saldo
                )
            )
            
            self.bd.terminaConexao()
        
