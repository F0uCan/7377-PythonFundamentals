## Herança.

class Pai:
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.nacionalidade = ''
        
    def falaNome(self): #camel case
        print(self.nome)

class Filha(Pai):
    def __init__(self):
        super().__init__()
        self.escolaridade = ''
    
    def falaEscolaridade(self):
        print('A minha escolaridade é', self.escolaridade)


class Neta(Filha):
    pass
    

### 

class automovel:
    pass
    
class barco:
    pass
    
class anfibio(automovel, barco):
    pass #herança múltipla
    
    

    



