# RPGs
## Polimorfismo
class Aprendiz:
    def __init__(self):
        self.nome = ''
        self.nivel = 0
        self.vida = 70
        self.magia = 0
        self.ataque = 0
        self.defesa = 0
        self.exp = 0
    
    def subirNivel(self):
        self.vida += 10
        self.magia +=1
        self.nivel +=1
        self.exp = 0
    
    def atacar(self):
        print("Eu não sei atacar :(")
        
    def defender(self):
        print('estou me defendendo')
        
    
class Arqueiro(Aprendiz):
    
    def atacar(self):
        print('Usar o arco e atacar de longe!')
    
    
    
class Mago(Aprendiz):
    
    def atacar(self):
        print('Vigarium levioza!')
    
class Cavaleiro(Aprendiz):

    def atacar(self):
        print('Sacou a espada e bateu!')
    
class ArquiMago(Mago):
    pass

## pokedex 
##
### Text Adventure 
### -> Escape 
### Colossal Cave Adventure




