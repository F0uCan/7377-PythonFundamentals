# Programação Orientada à Objetos

## Abstração
### -> capacidade de representar
#### elementos de negócio(contexto)
#### a nível de programação

## Contrato
#### voce irá receber elementos
#### os elemetos sao adicionados de forma sequencial
#### eu só consigo retirar o último elemento adicionado
#### eu consigo contar a quantidade de elementos

### Classe # Hiding .sort()
#atributos -> variáveis # características 
#métodos   -> funções   # comportamentos 

### Objeto # instância 
#implementação / cristalização da classe.
## Sintaxe base:

class Pilha:
    #construtor 
    def __init__(self): ## construtor com valor padrao
        self.__pilha = []
        self.__topo = 0
        
    def empilhar(self, item):
        # adicionar o item
        self.__pilha.append(item)
        self.__topo += 1
    
    def desempilhar(self):
        if self.__topo != 0:
            item_retirado = self.__pilha[-1]
            del self.__pilha[-1]
            self.__topo -= 1
            return item_retirado
            
        else:
            return 'pilha vazia'
            
    ## Getters and Setters
    def getTopo(self):
        return self.__topo
    
    
    def getPilha(self):
        return self.__pilha 
    


# criar um objeto
p1 = Pilha()

## Encapsulamento

## Herança 

## Polimorfismo
