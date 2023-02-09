vetor = []
i = 0
for r in range(50):
    valor = (i + 5 * i) % (i + 1)
    vetor.append(valor)
    i = i + 1
print(vetor)