
# cadastrar pessoas em dicionarios
## uma lista de cadastro a partir de registros em dicionario
### filtro para mostrar as pessoas que eram do estado de SP

### 1. Cadastrar pessoas em dicionario
### 2. Cadastrar em uma lista
### 3. Aplicar um filtro
### 4. Menu escolher em adicionar registros ou sair

# Reescreva  o programa

## funcao para cadastrar os usuarios
## mostrar um determinado registro da lista 
## filtrar a partir do estado ('SP') 
## funcao principal para controlar fluxo 

lista = []
 
def cadastro(lista):
    dic = {}
    dic['nome'] = input('Digite o Nome: ')
    dic['idade'] = int(input('Digite o Idade: ')) 
    dic['sexo'] = input('Digite o sexo: ')
    dic['cpf'] = input('Digite o CPF: ')
    dic['uf'] = input('Digite a UF: ')
    lista.append(dic)
    print('Registro Adicionado com Sucesso')


def mostrar_registro(lista):
    for registro in lista:
        print('--------------------')
        print('Nome:', registro['nome'])
        print('Idade:', registro['idade'])
        print('Sexo:', registro['sexo'])
        print('CPF:', registro['cpf'])
        print('UF:', registro['uf'])
  
def filtro_estado(lista):
    estado = input('Digite o Estado: ') 
    
    for registro in lista:
        if registro['uf'] == estado:        
            print('--------------------')
            print('Nome:', registro['nome'])
            print('Idade:', registro['idade'])
            print('Sexo:', registro['sexo'])
            print('CPF:', registro['cpf'])
            print('UF:', registro['uf'])
        
def main():
    while True:
        
        opcoes = {
            '1':cadastro, 
            '2':mostrar_registro, 
            '3':filtro_estado,
            '4': exit
        }
   
        print('Escolha a opcao:\n1 - Cadastrar Pessoa\n 2- Mostrar pessoas\n3- Filtro por Estado\n4- Sair\n')
        opcao = input('opcao: ')
        
        if opcao in opcoes.keys():
           opcoes[opcao](lista)
        else:
            print('Opcao invalida') 
        

if __name__ == '__main__':
    main()






# funcoes anonimas 'lambda'

exit()
soma = lambda num1,num2: num1 + num2 #argumentos: operacao 
soma(10,5) 
