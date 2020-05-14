## Escreva um programa que armazene um cadastro
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


def cadastrarTime(lista):
    """
    Recebe uma lista - OK 
    e insere um time no formato de dicionário
    """
    # Cria o dicionário e armazena as informações de time
    time = {}
    time['nome'] = input('Nome do Time: ')
    time['ntitulos'] = input('Quantidade de Títulos: ')
    time['conquistas'] = input('Principais Conquistas: ')
    time['mjogador'] = input('Melhor Jogador(a): ')
    time['gtorcida'] = input('Grito da Torcida: ')
    # insere o time na coleção (lista)
    lista.append(time)
    # mensagem de saída
    print('Time cadastrado com sucesso!')
    
    
def listarTimes(lista):
    """ 
    Recebe uma lista de times e apresenta as caracteristicas
    de cada time. 
    """# DocString
    for time in lista: 
        print('----------------------')
        print('Time:' , time['nome'])
        print('Quantidade de Títulos: ', time['ntitulos']) 
        print('Conquistas:', time['conquistas']) 
        print('Melhor Jogador:', time['mjogador']) 
        print('Grito da Torcida:', time['gtorcida'])
    
    
def buscaTime(lista):
    """
    Recebe uma lista de times e apresenta um time a partir
    da informação de melhor jogador da história informado
    pelo usuário
    """
    # captura a informação de jogador
    jogador = input('Informe o melhor da jogador: ')
    # buscar o jogador na lista de times 
    for time in lista: # lista = [{},{},{}]
        if jogador == time['mjogador']:
            # mostraTime(time) 
            ## Criar uma função para apresentar dados de um dic
            print('----------------------')
            print('Time:' , time['nome'])
            print('Quantidade de Títulos: ', time['ntitulos']) 
            print('Conquistas:', time['conquistas']) 
            print('Melhor Jogador:', time['mjogador']) 
            print('Grito da Torcida:', time['gtorcida'])
            break
    else:
        print('O jogador informado não está cadastrado na nossa base de times.')
    
def listarConquistas(lista):
    """
    Recebe uma lista de times e mostra as conquistas a
    partir de um time informado pelo usuário.
    """
    time = input('Informe o time para busca: ')
    
    for timeco in lista:
        if time == timeco['nome']:
            print('----------')
            print('Nome:', timeco['nome'])
            print('Conquistas:', timeco['conquistas']) 
    
        

def main(): # controlar o fluxo
    ## iniciar a lista de cadastro
    cad = []
    ## Estrutura de menu
    while True:
        dic_opcoes = {
            '1':cadastrarTime,
            '2':listarTimes,
            '3':buscaTime,
            '4':listarConquistas,
            '5':exit
        } 
        print('Escolha a opção desejada:\n1- Cadastrar Time\n2- Listar todos os Times\n3- Busca por Jogador\n4- Ver Conquistas\n5- Sair\n')
        op = input('')
        
        if op in dic_opcoes.keys():
            dic_opcoes[op](cad)
        else:
            print('Opção Inválida')
        
    
    
if __name__ == '__main__':
    main()
    
    
    ## {{time1}, {time2}, {time3}}
    ## lista = [{chaves:valores},{},{}]
    ## lista[0] = nome do time
    ## lista[1] = titulos... 
    
