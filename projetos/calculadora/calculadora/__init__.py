import funcoes

def calcule ():
    a = float(input('Informe o primeiro número: '))
    b = float(input('Informe o segundo número: '))

    operacao = (soma, subtracao, divisao, multiplicacao)

    opcao = int(input('''Digite a opção desejada:
                      \n 1 - Soma
                       \n 2 - Subtração
                        \n 3 - Divisão
                         \n 4 - Multiplicação '''))
    
    print(operacao(opcao - 1)(a, b))