# Aquecimento

## Exercícios:

## Dada a lista a seguir:
## [5,10,22,45,30,92,88,34,55]
### Escreva um script em python que :
lista = [5,10,22,45,30,92,88,34,55]
soma = 0
impar = 0
par = 0
# a) retornar a soma de todos os elementos

for elemento in lista:
    soma += elemento

print(soma, sum(lista))

# b) retornar a soma dos elementos pares
# c) retornar a soma dos elementos ímpares
for elemento in lista:
    if elemento % 2 == 0:
        par += elemento
    else:
        impar += elemento

print(f'Soma impar:{impar} \n' 
      f'Soma par: {par}')
      
# d) retornar a quantidade de elementos
cont = 0

for item in lista:
    cont += 1

print(cont, len(lista))


print('Elementos de índice PAR')
# e) mostrar os elementos de índice par
for indice in range(0,len(lista),2):
    print(lista[indice])

print('Elementos de Índice ímpar:')
# f) mostrar os elementos de índice ímpar
for indice in range(1,len(lista),2):
    print(lista[indice])



## A lista a seguir contém informações 
#  de um papel e sua variação de preços:
""" DocString
[('outubro/2000', 55.50'),
 ('novembro/2000', 35.20),
 ('dezembro/2000', 40.20),
 ('janeiro/2001', 50.00),
 ('fevereiro/2001', 52.20)
]
"""
## valor final/ valor inicial
# a) calcule a variação total
lista = [
 ('outubro/2000', 55.50),
 ('novembro/2000', 35.20),
 ('dezembro/2000', 40.20),
 ('janeiro/2001', 50.00),
 ('fevereiro/2001', 52.20)
]

# Acessar o primeiro elemento (valor inicial)
# Acessar o ultimo elemento (valor final)
# Efetuar o cálculo de varição 
lista2000=[]
print('Exercicio2:')

#var = lista[len(lista)-1]
var = (lista[-1][1] / lista[0][1]) - 1

print('{0:0.2f}'.format(var))
print(f'{var:0.2f}')
# b) calcule o percentual de variação do preço 
#    do papel para o ano de 2000
for item in lista:
    #validar elemento é do ano 2000
    if item[0].split('/')[1] == '2000':
          lista2000.append(item[1])
    #if item.endswith('2000'):
    
var2000 = (lista2000[-1] / lista2000[0]) - 1
# c) calcule o mesmo indicado para o ano de 2001
## Dica: testem o split;

lista2001 = []
for item in lista:
    #validar elemento é do ano 2000
    if item[0].split('/')[1] == '2001':
          lista2001.append(item[1])
    #if item.endswith('2000'):
    
var2001 = (lista2001[-1] / lista2001[0]) - 1

print(var2000, var2001)
