def fatorar_numero(numero):
    soma = 0
    for r in range(0, numero):
        if soma == 0:
            soma = numero * r
        else:
            soma = soma * r
    return soma
        
print(fatorar_numero(7))