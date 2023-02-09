def soma_algarismos(numero):
    soma = 0
    if numero > 0:
        num = list(str(numero))
        for number in range(len(num)):
            soma = soma + int(num[number])
        return f'A Soma dos números é {soma}'
    return 'Número Invalido'


print(soma_algarismos(1111111))

numero = 111111111
num = list(str(numero))
print(num)
