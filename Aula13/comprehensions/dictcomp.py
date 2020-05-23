# dicionarios a partir de expressões 

## aplicacao : transformar dados de arquivos em uma estrutura de dicionario.

#{'coluna': [linhas...]}

#0: abrir o arquivo
with open('data/sacramento.csv', 'rt') as arq:
    conteudo = arq.readlines()

#1: capturar o cabeçalho
cabec = conteudo[0].split(',')

#2: capturar todos dados por coluna... 
dados = [ [conteudo[linha].split(',')[coluna] for linha in range(1,len(conteudo))] for coluna in range(len(cabec))]

#3: associar cabec como chave ,dados como valor
dic_arquivo = {coluna: dado for coluna, dado in zip(cabec,dados)}

#4: Outra forma sem o dict:
outro_dic_arquivo = dict(zip(cabec,dados))

exit()
dic = { chr(65+num): num*num for num in range(10) }

def dict_comprehension(num):
    dic = {}
    for numero in range(num):
        dic[chr(65+numero)] = numero * numero
    return dic
    
