vetor = []
for r in range(20):
    valor = int(input("Informe um Valor"))
    vetor.append(valor)
    if valor in vetor:
        quantidade = vetor.count(valor)
        if quantidade > 1:
            vetor.pop(vetor.index(valor))
print(vetor)