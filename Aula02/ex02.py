# Coleções 

dicionario = {
    'Morango': 3.50,
    'Banana': 2.20,
    'Melancia':5.00
}



dicionario['palavra'] # 'significado


exit()
# 1: Definição das variáveis
cesta = []
valores = [3.50, 2.20, 5.00]
soma = 0
# processamento
while True:
    print('Escolha o seu produto:')
    
    produto = input('1- Morango (3.50), 2- Banana, 3- Melancia, 4 - sair')
    
    if produto == '1':
        cesta.append('Morango')
    elif produto == '2':
        cesta.append('Banana')
    elif produto == '3':
        cesta.append('Melancia')
    elif produto == '4':
        break

print(cesta)
for fruta in cesta:
    if fruta == 'Morango':
        soma += valores[0]
    elif fruta == 'Melancia':
        soma += valores[1]
    else:
        soma += valores[2]
# Saida
print('O total da compra foi de :', soma)

exit()
#list()
            #0        #1   #2
lista = ['Guilherme', 32, 'SP']
#primeiro elemento

print(lista[1]) 

### comportamentos

# inserção
lista.append('José')

# remover
lista.pop()
#del lista[0] 

lista.sort()
# Estruturas de repetição

lista[0] = 'Carlos' 
exit()
## FOR        # [0,11[ 
              # 0,1,2,3,4,5,6,7,8,9,10

lista = ['manga', 'banana', 'melancia']
for fruta in lista:
    print(fruta)

## para cara numero no intervalor 0-10
for jujuba in range(0,11): 
    print(jujuba)

## numero = 0
## print(numero)

## numero = 1
## print(nuemero) 

exit()
while True:
    # 1. Capturar os números
    num1 = float(input('N1: '))
    num2 = float(input('N2: '))

    # 2. Escolher o tipo de calculo
    opcao = input('Escolha a opção Desejada:\n1- Soma\n2- Sub\n3 - Mult\n4 - Div\n5 - Sair\n')

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
    elif opcao == '5':
        print('Obrigado')
        break
    else:
        print('Opção Inválida')
    

exit()
## while 
contagem = 0

while contagem <= 10:
    print(contagem)
    contagem += 1



print('Sai do while')
## for 
