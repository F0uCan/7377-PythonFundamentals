# Controle de Fluxo

# Criar uma calculadora em python
## Deverá realizar soma, subtração, multiplicação e divisão
## O usuário deverá escolher a opção 1 - Soma, 2 - Sub, 3- Mult. 4 Div
## Opcao invalida

# 1. Capturar os números
num1 = float(input('N1: '))
num2 = float(input('N2: '))

# 2. Escolher o tipo de calculo

opcao = input('Escolha a opção Desejada:\n1- Soma\n2- Sub\n3 - Mult\n4 - Div')

# 3. Executar de acordo a opção

if opcao == "1":
    print(num1+num2)
elif opcao == '2':
    print(num1-num2)
elif opcao == '3':
    print(num1*num2)
elif opcao == '4':
    if not num2 == 0:
        print(num1/num2)
    else:
        print('Não dividirás por Zero')
else:
    print('Opção Inválida')
    
exit()
# múltilplas condições

## Crie um script em python que retorne o seu IMC

## IMC = PESO / ALTURA ** 



### IMC < 18.5 - Magreza
### 18.5 < IMC 24.9 - Normal
### 25 < IMC < 29.9 - Sobrepeso
### 30 < IMC < 39.9 - Obesidade
### IMC > 40 - Obesidade Grave 


## 
# 1. Capturar Peso e Altura
peso = float(input('Informe o peso:'))
altura = float(input('Informe sua altura :'))

# 2. Calcular o IMC
imc = peso/(altura**2)

print(imc) 
# 3. Comparar o IMC com as referencias 
if imc <= 18.5:
    # 4. Informar ao usuário a classificação
    print('IMC - Magreza')
elif imc < 24.9:
    print('IMC - Normal')
elif imc < 29.9:
    print('IMC - Sobrepeso')
elif imc < 39.9:
    print('IMC - Obesidade')
else:
    print('IMC - Obesidade Grave')




exit()
## > < != == >= <=

## 1. Capturar a idade
idade = int(input('Informe a sua idade: '))

## 2. Capturar a informação de Hab.
hab = input('Possui Habilitação? S/N:')

## 1. precisa ter idade >= 18
if idade >= 18 and hab.upper() == 'S':
    ## 2. precisa ter habilitação
    #if hab == 'S':
    print('Pode Dirigir')
else:
    print('Não Pode Dirigir')        
    

        
