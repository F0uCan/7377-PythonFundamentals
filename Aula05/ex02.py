## Exercícios Utilizando funções

#1) Escreva um programa em python que calcule a média
## de um aluno e diga se está aprovado, reprovado ou
## em recuperação.
## A média do aluno é composta por 3 notas 
## Um aluno é reprovado direto se obtiver nota 
## inferior ou igual a 4
## Um aluno está de recuperação se obtiver notas
## entre 4.1 e 5.99 
## Um aluno está aprovado se obtiver nota maior do que 6

def calculaMedia(*notas):
    #return (nota1 + nota2 + nota3)/3
    soma = 0
    for nota in notas: # sum(notas)
        soma += nota
    return soma/len(notas)
    
def validaAprovacao(nota):
    if nota <= 4:
        print('Reprovado')
    elif nota < 6:
        print('Em Recuperação')
    else:
        print('Aprovado')

def main():
    # capturar as notas (3)
    n1 = float(input('N1 :'))
    n2 = float(input('N2 :'))
    n3 = float(input('N3 :'))
    
    # calculo da media
    media = calculaMedia(n1,n2,n3) 
    
    # validação se foi aprovado
    validaAprovacao(media)
    

if __name__ == '__main__':
    main()
    
    
