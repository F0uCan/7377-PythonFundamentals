#classe de menu
from caixaEletronico import *
from getpass import getpass
from caixaEletronico.SQL.query import query_entrar

class MenuCaixa:
    def __init__(self):
        self.opcoes = {}
        self.login = ''
        self.password = ''
    
    def menuCliente(self, usuario_id):
        
        cliente = Cliente()
        cliente.login = usuario_id 
        
        self.opcoes = {
            '1': cliente.redefinirSenha,
            '2': cliente.consultarSaldo,
            '3': cliente.realizarSaque,
            '4': cliente.realizarDeposito,
            '5': cliente.realizarTransferencia,
            '6': self.menuPrincipal
        }
        while True:
            op = input(f'Bem vindo ao Caixa Eletrônico\n' \
                       f'Digite a opção desejada:\n1- Mudar Senha' \
                       f'\n2- Saldo' \
                       f'\n3- Saque' \
                       f'\n4- Depósito' \
                       f'\n5- Transferencia' \
                       f'\n6- Sair\n')
            try:
                self.opcoes[op]()          
            except KeyError as err:
                print('Opção inválida')
        
        
    def menuAdmin(self):
        
        admin = Admin()
        self.opcoes = {
            '1': admin.cadUsuario,
            '2': admin.resetSenha,
            '3': admin.desbloquearUsuario,
            '4': admin.cadConta,
            '5': self.menuPrincipal
        
        }
        while True:
            op = input(f'CE - Admin\n' \
                       f'Digite a opção desejada:\n1- Cadastrar novo Usuário' \
                       f'\n2- Resetar Senha' \
                       f'\n3- Desbloquear Usuário' \
                       f'\n4- Cadastrar Conta' \
                       f'\n5- Retornar ao Menu Principal\n')
                       
            try:
                self.opcoes[op]()
            except KeyError as err:
                print('Opção inválida')
        
        
        
    def menuPrincipal(self):
        self.opcoes = {
            '1': self.entrar,
            '2': exit
        }
        
        while True:
            op = input("Digite a Opção Desejada:\n1- Entrar\n2- Sair\n")
            try:
                self.opcoes[op]()
            except KeyError as err:
                print("Opção inválida")
    
    
    def entrar(self):
        self.login = input("Usuário: ")
        self.password = getpass("Senha: ")        
        
        bd = ConexaoBanco()
        
        try:
            bd.iniciaConexao()
        
        except Exception as err:
            print("Erro ao conectar no Banco de Dados", err)
        
        else:
            resultado = bd.executaSQL(query_entrar.format(self.login))
            
            for registro in resultado:
                if registro['login'] == self.login and registro['senha'] == self.password:
                    if registro['admin']:
                        self.menuAdmin()
                    else:
                        self.menuCliente(registro['id'])
                else:
                    print('Usuário ou Senha Inválidos')
                    break
            else:
                print("Usuário não encontrado em nossa base de dados")
            
            bd.terminaConexao()
            
            
if __name__ == '__main__':
    MenuCaixa().menuPrincipal()
