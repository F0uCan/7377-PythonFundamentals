## trabalhando com arquivos - exemplos 

## txt 
## csv padrão organização dos dados
## json { 'coluna1': [linha1,linha2,linha3, .....]  }
## xml <pessoa><nome>nome dapessoa</nome> </pessoa>

## consulta

## 1- Abrir o arquivo
## 2- Carregar o conteudo do arquivo

with open('data/cadastro.csv' , 'r') as arquivo:
    conteudo = arquivo.readlines()

## 3- Encontrar o registro que informei pelo nome
nome = input('Informe o nome para busca: ')

for linha in conteudo:
    #print(linha)
    if nome in linha.split(','):
        print('------------')
        print(linha.split(',')[0])
        print(linha.split(',')[1])
        print(linha.split(',')[2])
        print(linha.split(',')[3])
        break
else:
    print('Nenhum registro foi encontrado') 


## 4- Apresentar o registro em tela (todos os campos)


exit()
diretorio = 'data/cadastro.csv'

# captura informações
nome = input('Digite o nome: ')
sobrenome = input('Digite o Sobrenome: ')
idade = input('Digite a Idade: ')
cpf = input('Digite o CPF: ')

cabec = 'nome,sobrenome,idade,cpf\n'
registro = f'{nome},{sobrenome},{idade},{cpf}\n'

registro_final = cabec+registro 
### 
with open(diretorio, 'w') as arquivo:
    arquivo.write(registro_final)
    
