# Crie uma classe que
## represente um carro

### atributos:
## velocidade
## cor
## marca
## ano 

### comportamentos:
## acelerar
## frear 
## ligar a seta 
## buzinar

from random import randint, shuffle


class Carro:
    ## atributos
    def __init__(self, velocidade=0, cor='',marca='',ano=0, potencia=0.0):
        self.velocidade = velocidade
        self.cor = cor
        self.marca = marca
        self.ano = ano
        self.km = 0
        self.potencia = potencia
        
    ## comportamentos
    
    def acelerar(self, velocidade=10):
        self.velocidade += velocidade * self.potencia
        self.km += self.velocidade

    def frear(self, velocidade=10):
        self.velocidade -= velocidade

    def ligarSeta(self, direcao):
        print('ligou a seta da', direcao)
        
    def buzinar(self):
        print('FOOOOOOOOOOOOOOOOOOOOOOM')
        

## Classe Corrida

class Corrida:
    def __init__(self):
        self.numero_voltas = 20
        self.tamanho = 2000
        self.num_pits = 2
        self.grid_final = []
        self.grid_inicial = []
        self.largada = False
        self.bandeirada = False
        
    def adicionarNoGrid(self, *args):
        for carro in args:
            self.grid_inicial.append(carro)    
        
    def iniciarCorrida(self):
        self.largada = True
        print('COMEÇOU!')
    
    
    def encerrarCorrida(self, num_voltas):
        if self.numero_voltas == num_voltas:
            self.bandeirada = True
    
    def verificarGanhador(self, lista_carros):
        km = 0
        
        for carro in lista_carros:
            if carro.km > km:
                km = carro.km
        
        ## km do vencedor
        for carro in lista_carros:
            if carro.km == km:
                print('O carro' , carro.marca,' foi o vencedor')
                break
        
        
                
    def principal(self):
        ## criei os carros
        c1 = Carro(0, 'Amarelo','Lotus',1976, 1.5)
        c2 = Carro(0, 'Vermelho','Ferrari',1978, 1.8)
        c3 = Carro(0, 'Azul','Williams',1992, 1.6)
        ## adicionei no grid
        self.adicionarNoGrid(c1,c2,c3)
        
        ## iniciar a corrida
        
        while self.bandeirada == False:
            
            for carro in self.grid_inicial:
                if carro.velocidade >= 250:
                    carro.frear(randint(40,50))
                else:
                    carro.acelerar(randint(50,60))
            
            print('Parciais - Volta')
            for carro in self.grid_inicial:
                print(carro.marca, carro.km)
            
            print('---------------------')
        
            ## final de volta
            self.numero_voltas -= 1
            
            ## verifica o número de voltas 
            if self.numero_voltas == 0:
                self.bandeirada = True
                
        ## Avaliar quem ganhou?
        self.verificarGanhador(self.grid_inicial)


if __name__ == '__main__':
    corrida = Corrida()
    corrida.principal()
    
    
