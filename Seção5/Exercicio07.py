vetor = []
for r in range(10):
    valor = int(input("Informe um valor: "))
    vetor.append(valor)
print(vetor)
print("O Maior Elemento do vetor é {0} e se encontra na posição {1}".format(max(vetor), vetor.index(max(vetor))))