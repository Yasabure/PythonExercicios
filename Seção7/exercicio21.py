def numero_primo(numero):
    numerosprimos = [2, 3, 5, 7, 11]
    primos =[]
    for r in range(0, numero):
        for numeros in numerosprimos:
            if r % numeros != 0 or r % numeros == numeros:
                primos.append(r)
                if r > 11:
                    numerosprimos.append(r)

print(numero_primo(10))

c