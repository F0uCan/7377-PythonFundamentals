from BD import ConexaoBanco

class Usuario:
    def __init__(self):
        self.nome =''
        self.sobrenome =''
        self.email =''
        self.login = ''
        self.password = ''
        self.reset = 1
        self.tentativas = 0
        self.admin = False
        
        
class Admin(Usuario):
    def __init__(self):
        super().__init__()
        self.admin = True
    
    def cadUsuario(self):
        pass
        
    def resetSenha(self):
        pass
    
    def dUsuario(self):
        pass
        
class Cliente(Usuario):
    
    def redefinirSenha(self):
        pass
    
    def consultarSaldo(self):
        pass    
    
    def realizarSaque(self):
        pass
        
    def realizarDeposito(self):
        pass
        
    def realizarTransferencia(self):
        pass
        
if __name__ == '__main__':
    admin = Admin()
    cliente = Cliente()
