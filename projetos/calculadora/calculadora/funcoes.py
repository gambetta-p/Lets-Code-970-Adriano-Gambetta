def soma (a, b):
    try:
        return a + b
    except:
        raise TypeError(f'O input "a" e "b" devem ser uma string, int ou float, recebido {a}, {type(a)}, {b} {type(b)}')

def subtracao (a, b):
    return a - b

def divisao (a, b):
    if b != 0:
        return a/b
    else:
        print('Divisão inválida')

def multiplicacao (a, b):
    try:
        return a * b
    except:
        raise TypeError(f'O input "a" e "b" devem ser uma string, int ou float, recebido {a}, {type(a)}, {b} {type(b)}')