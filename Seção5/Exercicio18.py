vetor = []
mult = []
for r in range(10):
    valor = int(input("Informe um Valor: "))
    vetor.append(valor)
x = int(input("Informe o valor de X: "))
i = 0
for r in range(10):
    i = i + 1
    if x * i in vetor:
        mult.append(x * i)
print(mult)


 