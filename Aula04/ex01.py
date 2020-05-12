#Funções

## calc

def soma(num1, num2):
    return num1+num2

def subtracao(num1, num2):
    return num1 - num2
    
def multiplicacao(num1,  num2):
    return num1 * num2
    
def divisao(num1,num2):
    if num2 != 0:
        return num1/num2
    else:
        print('Não Dividirás por zero')



## fluxo

def main():
    num1 = float(input())
    num2 = float(input())
    opcao = input()
    
    dic_opcoes = {
        '1': soma,
        '2': subtracao,
        '3': multiplicacao,
        '4': divisao
    }
    
    if opcao in dic_opcoes.keys():
        print(dic_opcoes[opcao](num1,num2))
    else:
        print('opcao invalida')
    

if __name__ == '__main__':
    main()


exit()
##Variaveis globais EVITEM AO MAXIMO

TAXA_JUROS = 0.25
PI = 3.141516

def soma(num1, num2): #parametro com valor padrao
    adicao = num1+num2
    return adicao * taxa #(15
    
## escopo

res = soma(10) # argumentos



exit()
## Uso de funções nativas

input() #chamada de função
print()
sum()
int()
str()
float() 

## funções a partir de módulos externos

from random import randint

randint(1,6)

## funções customizadas (User Defined functions) 
 
def saudacao():
    print('Olá Tudo bem')
    
def sauda_acao():
    return 'Olá Tudo bem'
    



 
 
