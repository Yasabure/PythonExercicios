from msilib.schema import Error


def contas(a: int,b: int):
    if b < 0:
        return print(Error)
    print('Escolha a Operação: Divisão (1), Negativo(2), Subtração(3), Soma(4), Multiplicação(5)')
    operação = int(input('Operação: '))

    if operação == 1:
        print(a/b)
    elif operação == 2:
        print(a - (a*2))
    elif operação == 3:
        print(a-b)
    elif operação == 4:
        print(a+b)
    elif operação == 5:
        print(a*b)

contas(3, 2)