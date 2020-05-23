## aplicações 
from random import randint

### abertura do arquivo

with open('data/sacramento.csv', 'rt') as arq:
    conteudo = arq.readlines() ## lista de strings que representam um registro
# aplicar filtros em conteúdo de arquivos

imoveis = [conteudo[randint(1,len(conteudo)-1)] for x in range(1,100) if float(conteudo[x].split(',')[9]) > 100000]


exit()
# exemplo gerar amostras aleatórias
amostra = [conteudo[randint(1,len(conteudo)-1)] for x in range(50)]

for indice in range(5):
    print(amostra[indice])

exit()
def mostra_sequencia(num):
    lista = []
    for numero in range(num):
        lista.append(numero)
    return lista
    
    
lista = mostra_sequencia(10)
nova_lista = [ numero for numero in range(10) ]
quadrados = [numero * numero for numero in range(100)]

