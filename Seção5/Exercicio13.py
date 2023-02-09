vetor = []
for r in range(5):
    valor = int(input("Informe um valor: "))
    vetor.append(valor)
print("O Maior Número Se encontra na posição {0} e o Menor {1}".format(vetor.index(max(vetor)), vetor.index(min(vetor))))