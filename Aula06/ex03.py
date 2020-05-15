## Arquivos

## Exercícios:

### Escreva um programa em python que armazene um cadastro
### de filmes em um arquivo de texto,csv(;),tabulacao
### Os campos a serem armazenados são:
#### - título
#### - ano
#### - diretor(a)
#### - roteirista
#### - atores 
####  imdb.com


### b) implemente a funcionalidade de consulta por título
### c) implemente a funcionalidade de alteração do registro
### d) implemente a funcionalidade de remoção do registro



def cadastrarFilme():
    """
    Insere informações de filme em um arquivo csv.
    """
    # Cria o dicionário e armazena as informações de filme

    titulo = input('Nome: ')
    ano = input('Ano: ')
    diretor = input('Diretor(a): ')
    roteirista = input('Roteirista: ')
    atores = input('Atores: ')
    
    # formato específico de valores separados entre vírgula com uma quebra de linha
    registro = f'{titulo},{ano},{diretor},{roteirista},{atores}\n'
    
    # insere o filme no arquivo csv
    with open('data/filmes.csv' , 'a') as arquivo: 
        conteudo = arquivo.write(registro)

    # mensagem de saída
    print('Filme cadastrado com sucesso!')
    
    
def buscarFilme():
    """ 
    Busca um filme a partir do seu título no arquivo csv.
    """# DocString
    ## Capturo o nome de busca
    nome = input('Infome o título do filme :')
    
    ## Abertura do arquivo para pesquisa
    with open('data/filmes.csv', 'r') as arquivo:
        conteudo = arquivo.readlines()    
    
    for filme in conteudo:
        if nome in filme.split(','):
            rfilme = filme.split(',')
            print('----------------------')
            print('Título:' , rfilme[0])
            print('Ano: ', rfilme[1]) 
            print('Diretor(a):', rfilme[2]) 
            print('Roteirista:', rfilme[3]) 
            print('Atores:', rfilme[4])
    
    
def atualizarFilme():
    """
    Realiza uma busca no arquivo de filmes e
    caso encontrar o filme desejado, direciona para a 
    atualização
    """
    # captura a informação de filme 
    nome = input('Infome o título do filme :')
    
    ## Abertura do arquivo para pesquisa
    with open('data/filmes.csv', 'r') as arquivo:
        conteudo = arquivo.readlines()    
    
    
    for linha in range(len(conteudo)):
        if nome in conteudo[linha].split(','):
            rfilme = conteudo[linha].split(',')
            print('----------------------')
            print('Título:' , rfilme[0])
            print('Ano: ', rfilme[1]) 
            print('Diretor(a):', rfilme[2]) 
            print('Roteirista:', rfilme[3]) 
            print('Atores:', rfilme[4])
            
            print('Você deseja Atualizar o filme? S/N')
            
            if input('') == 'S':
                ### atualização
                
                ### candidato à função
                titulo = input('Nome: ')
                ano = input('Ano: ')
                diretor = input('Diretor(a): ')
                roteirista = input('Roteirista: ')
                atores = input('Atores: ')
                # formato do arquivo csv
                registro = f'{titulo},{ano},{diretor},{roteirista},{atores}'
                #registro = "{},{},{},{},{},{}".format(variaveis...)
                conteudo[linha] = registro
                
                ## persistencia
                
                with open('data/filmes.csv', 'w') as arquivo:
                    arquivo.write('\n'.join(conteudo))
                    
                break
            else:
                print('Cancelado pelo usuário')
                break
    else:
        print('O filme informado não está cadastrado na nossa base de dados.')
    
def removerFilme():
    """
    Realiza uma busca no arquivo de filmes e
    caso encontrar o filme desejado valida se deseja
    remover o filme.
    """
    # captura a informação de filme 
    nome = input('Infome o título do filme :')
    
    ## Abertura do arquivo para pesquisa
    with open('data/filmes.csv', 'r') as arquivo:
        conteudo = arquivo.readlines()    
    
    
    for linha in range(len(conteudo)):
        if nome in conteudo[linha].split(','):
            rfilme = conteudo[linha].split(',')
            print('----------------------')
            print('Título:' , rfilme[0])
            print('Ano: ', rfilme[1]) 
            print('Diretor(a):', rfilme[2]) 
            print('Roteirista:', rfilme[3]) 
            print('Atores:', rfilme[4])
            
            print('Você deseja Remover o filme? S/N')
            
            if input('') == 'S':
                del conteudo[linha]
                
                #persistencia 
                with open('data/filmes.csv', 'w') as arquivo:
                    arquivo.write('\n'.join(conteudo))
                break
                
            else:
                print('Cancelado pelo usuário')
                break
    else:       
        print('O filme não foi encontrado.')
        

def main(): # controlar o fluxo
    ## Estrutura de menu
    while True:
        dic_opcoes = {
            '1':cadastrarFilme, #camelCase 
            '2':buscarFilme,
            '3':atualizarFilme,
            '4':removerFilme,
            '5':exit
        } 
        print('Escolha a opção desejada:\n1- Cadastrar Filme\n2- Buscar Filme\n3- Atualizar Filme\n4- Remover Filme\n5- Sair\n')
        op = input('')
        
        if op in dic_opcoes.keys():
            dic_opcoes[op]()
        else:
            print('Opção Inválida')
        
    
    
if __name__ == '__main__':
    main()








