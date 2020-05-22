#classe de menu
from getpass import getpass
from BD import ConexaoBanco
from .SQL.query import query_entrar


class MenuCaixa:
    def __init__(self):
        self.opcoes = {}
        self.login = ''
        self.password = ''
    
    def menuCliente():
        self.opcoes = {
            '1': 'redefinir senha',
            '2': 'consultar saldo',
            '3': 'realizar saque',
            '4': 'realizar depósito',
            '5': 'realizar transferencia',
            '6': self.MenuPrincipal
        }
        while True:
            op = input(f'Digite a opção desejada:\n1- Mudar Senha'
                       f'\n2- Saldo' \
                       f'\n3- Saque' \
                       f'\n4- Depósito' \
                       f'\n5- Transferencia' \
                       f'\n6- Retornar ao menu Principal')
                       
             try:
                 self.opcoes[op]()          
             except KeyError as err:
                 print('Opção inválida')
        
        
    def menuAdmin(self):
        self.opcoes = {
            '1': 'Cadastrar novo Usuário',
            '2': 'Resetar Senha',
            '3': 'Desbloquear usuário',
            '4': 'Retornar ao Menu Principal'
        
        }
        while True:
            op = input(f'Digite a opção desejada:\n1- Cadastrar novo Usuário' \
                       f'\n2- Resetar Senha' \
                       f'\n3- Desbloquear Usuário' \
                       f'\n4- Retornar ao Menu Principal')
                       
             try:
                 self.opcoes[op]()          
             except KeyError as err:
                 print('Opção inválida')
        
        
        
    

    def menuPrincipal(self):
        self.opcoes = {
            '1': self.entrar,
            '2': 'Sair'
        }
        
        while True:
            op = input("Digite a Opção Desejada:\n1- Entrar\n2- Sair")
            
            try:
                self.opcoes[op]()
    
    def entrar(self):
        self.login = input("Usuário: ")
        self.password = getpass("Senha: ")        
        
        bd = ConexaoBanco()
        
        try:
            bd.iniciaConexao()
        
        except Exception as err:
            print("Erro ao conectar no Banco de Dados")
        
        else:
            
            resultado = bd.executaSQL(query_entrar.format(login)
            
            temNoBanco = True
            #### validação via banco de dados.
            if temNoBanco:
            ### iniciar o banco
            ### realizar uma consulta com os dados informados
            ### caso o retorno for positivo eu redireciono conforme o tipo.
                admin = True
                if admin:
                    self.menuAdmin()
                else:
                    self.menuCliente()
            else:
                print("Usuário ou Senha Inválidos")
            
