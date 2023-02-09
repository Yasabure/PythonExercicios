def triangulo_lateral(numero: int):
    for r in range(1, numero + 1):
        print('*' * r)
        if r == numero:
            for i in range(1, numero + 1):
                print('*' * (numero - i))

triangulo_lateral(6)