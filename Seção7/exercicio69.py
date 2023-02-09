from fractions import Fraction


def a1 (a,b,c,d) -> int:
    p = Fraction(a,b)
    q = Fraction(c,d)
    lista = [a, b, c, d]
    listaMDC = []
    for i in range(0,2):
        r = 0
        if i > 0:
            r = 2
        mdc = lista[0+r]
        while lista[0+r] % mdc != 0 or lista[1+r] % mdc !=0:
             mdc = mdc -1
        listaMDC.append(mdc)
    
    a /=listaMDC[0]
    b /=listaMDC[0]
    c /=listaMDC[1]
    d /=listaMDC[1]
    
    print(f'Soma: {p + q}, Subtração: {p - q}, Divisão: {p /q}, Multiplicação: {p*q}')


a1(10,12,6,4)
