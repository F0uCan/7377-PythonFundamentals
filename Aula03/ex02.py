# Dicionários

#1) Escreva um script em Python que registre 
# dados cadastrais em um dicionário
## Os dados a serem coletados são:
# - nome
# - idade
# - sexo
# - cpf
# - estado

# input
## dic['chave'] = valor

dic = {}
        dic['nome'] = input('Digite o Nome: ')
        dic['idade'] = int(input('Digite o Idade: ')) 
        dic['sexo'] = input('Digite o sexo: ')
        dic['cpf'] = input('Digite o CPF: ')
        dic['uf'] = input('Digite a UF: ')



#notação de acesso dos dicionarios


#2) Escreva um Script em Python que possa armazenar
# múltiplos registros do exercício anterior em uma
# lista. Você deverá criar um menu para cadastrar os
#registros
pessoas = []

while True:
    print('Cadastro')
    opcao = input('Escolha a Ação:1 - Cadastrar, 2-Sair')
    
    if opcao == '1':
        dic = {}
        dic['nome'] = input('Digite o Nome: ')
        dic['idade'] = int(input('Digite o Idade: ')) 
        dic['sexo'] = input('Digite o sexo: ')
        dic['cpf'] = input('Digite o CPF: ')
        dic['uf'] = input('Digite a UF: ')
        
        pessoas.append(dic)
    elif opcao == '2':
        break
    else:
        print('Opção Inválida')

# while true
# 3) A partir da lista resultante do exercício 2, 
# escreva um script em python que mostre a idade
# das pessoas cujo estado é 'SP'

# pessoas = [{},{},{}]

#1 Varredura na lista

for documento in pessoas:
    #2 Validar se a pessoa mora em sao paulo
    if documento['uf'].upper() == 'SP':
    #3 apresento a idade da pessoa
        print('---------------')
        print('Idade :', documento['idade'])
print('Olá')




