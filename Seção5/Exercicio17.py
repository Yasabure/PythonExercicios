vetor = []
for r in range(10):
    valor = int(input("Informe um Valor: "))
    if valor < 0:
        valor = 0
        vetor.append(valor)
    else:
        vetor.append(valor)
print(vetor)