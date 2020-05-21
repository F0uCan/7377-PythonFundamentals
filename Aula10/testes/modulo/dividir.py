def div(num1,num2):
    try:
        res = num1/num2
    except ZeroDivisionError as err:
        return 'Não dividirás por zero'
    else:
        return res
        
