#2) Escreva um programa em python que retorne o valor
## mínimo de uma lista. 
### utilize a lista a seguir como referência:
# [0,-1,55,13,45,2,-3]

def retMin(lista):
    minimo = lista[0]
    for valor in lista:
        if valor < minimo:
            minimo = valor
    return minimo

def retMax(lista):
    maximo = lista[0]
    for valor in lista:
        if valor > maximo:
            maximo = valor
    return maximo

    
def main():
    nova_lista = [0,-1,55,13,45,2,-3]
    
    ## chamada f. descobrir o mínimo
    print(retMin(nova_lista))
    
    ## chamada f. descobrir o mínimo
    print(retMax(nova_lista)) 

if __name__ == '__main__':
    main()

### implemente retorno do menor valor par da lista
### implemente retorno do menor valor impar
### implemente um programa em python o qual o usuário pode
### digitar o quanto quiser e que ao final seja mostrado:

##  O maior número
##  O menor número
##  O maior número par
##  O menor número ímpar

### While True + Break -> armazenaria as informações em uma lista
### processaria a lista em uma função.

## modularizado em funcoes

## principal que fornece a lista
## funcao que retorna o valor mínimo


#3) Escreva um programa em python que retorne o valor
# máximo de uma lista
### utilize a lista a seguir como referência:
# [0,-1,55,13,45,2,-3]
