#arquivos 


## contexto
with open('teste.txt', 'r') as arquivo: 
    conteudo = arquivo.read()

## sai da identação    

## salvar informação 
with open('teste.txt', 'a') as arquivo:
    arquivo.write('texto a ser inserido') 


exit()
## txt / .dat
## SGBD 

## criando arquivos com python

## abertura do arquivo
arquivo = open('teste.txt', 'r')
## capturei a informacao do arquivo
conteudo = arquivo.read() # le todo o conteúdo do arquivo, armazena em uma string
#conteudo = arquivo.readlines() #converte cada linha em um elemento e armazena na lista
arquivo.close()

conteudo += ' !!!!!!!'

### depreciada!
arquivo = open('teste.txt', 'w')
arquivo.write(conteudo)
arquivo.close() 

### r = Read
### w = Write
### a = Append 
### x = eXclusivo
## CUIDADO com o w

 



