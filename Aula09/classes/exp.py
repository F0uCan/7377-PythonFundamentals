# tratamento 

## pediu para abrir um arquivo que nao existe

## try: tentativa de execução do código que pode quebrar.
## except tratativas caso o código não seja bem sucedido
## else: tratativas caso o código seja bem sucedido
## finally: sempre executa após o trecho de try/except/else


def func1():
    print('1')

def func2():
    print('2')
    
def func3():
    print('3')


opcoes = {
        '1': func1,
        '2': func2,
        '3': func3,
        '4': exit
   
   }

while True:
    op = input('Escolha a opção desejada')
    
    try:
        opcoes[op]()
    except KeyError as erro:
        print("Opção Inválida, escolha novamente")
   



    
    
