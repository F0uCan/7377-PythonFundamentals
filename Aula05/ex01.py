### Revisitando funções

#visibilidade

#tipos mutáveis e tipos imutáveis

### tipos imutáveis: int, floats, strings, tuplas 

def atualizaTexto(string):
    novo_texto = string + " !!!!"
    return novo_texto 
    
texto = "4Linux Open Software Specialists"
texto = atualizaTexto(texto)
print(texto)

## Em python, para se realizar a atualização de valores envolvendo
## tipos imutáveis como strings, ints, tuplas e floats por exemplo
## é necessário realizar uma nova atribuição.
## Quando utilizamos funções, essa atribuição será realizada através
## do retorno do valor da função com a instrução return.

exit()

# tipos mutaveis : dicionarios, listas 
 

def atualizaLista(lista): #passagem por referencia
    lista.append('novo valor')

lista_qualquer = ['valor antigo']

atualizaLista(lista_qualquer)
print(lista_qualquer) 

#  novo valor e valor antigo, valor antigo, ERRO?
## como a lista é um tipo mutável, o python aceita modificações mesmo
## estando fora do escopo, ou o que tradicionalmente chamados em outra
## linguagem de passagem por referência. Isso se aplica aos tipos 
## mutáveis como dictionários e listas.

exit()
def inc1(num):
    num += 1
    return num
    
num1 = 10
num1 = inc1(num1)
num1 = inc1(num1)
print(num1) # 10, 11, Erro????



exit()
## como a variável foi definida antes da função,
## o python a interpreta com variável global, e
## assim todas as funções enxergam a variável.

variavel_global = [0] #variável global EVITEM <--
x = 10

def fun1():
    variavel_global[0] +=x
    

def fun2():
    variavel_global[0] +=x

def fun3():
    variavel_global[0] +=x

fun1()
fun2()
fun3()
print(variavel_global)


exit()
## Sintaxe Básica

def nomeFuncao(parametros):
    pass

## Parâmetros/Argumentos
nomeFuncao(argumento)

## Parâmetros dinâmicos 
### *args

def soma(*jujuba):
    res = 0
    for num in jujuba:
        res += num
    return res

soma(1,2)
soma(1,2,3,4)

### **kwargs keyword arguments

def soma(**kwargs):
    pass


## Tipos de dados e passagem de parâmetro

### Exercícios

#2) Escreva um programa em python que retorne o valor
## mínimo de uma lista. 
### utilize a lista a seguir como referência:
# [0,-1,55,13,45,2,-3]

## modularizado em funcoes

## principal que fornece a lista
## funcao que retorna o valor mínimo


#3) Escreva um programa em python que retorne o valor
# máximo de uma lista
### utilize a lista a seguir como referência:
# [0,-1,55,13,45,2,-3]


##4) Escreva um programa que armazene um cadastro
## em uma lista. O cadastro deverá ser composto por:
## - Time:
## - Número de Títulos
## - Principais Conquistas
## - Melhor Jogador(a) da História
## - Grito da Torcida

#a) o seu programa deverá implementar as seguintes
## funcionalidades: 
### - mostrar todos os times cadastrados
### - mostrar o time a partir do jogador informado (caso existir)
### - listar conquistas a partir de um time 

