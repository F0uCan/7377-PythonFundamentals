def soma(num1, num2):
    """
    Recebe dois números e retorna a soma
    entre eles.
    
    """
    return num1+num2

def soma_multipla(*args):
    """
    Recebe n números, e retorna soma de todos
    eles.
    """
    res = 0
    for numero in args:
        res += numero
    return res
