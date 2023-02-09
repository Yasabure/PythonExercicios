vetor = []
for r in range(15):
    nota = float(input("Informe a Nota da Prova: "))
    vetor.append(nota)
print(sum(vetor) % len(vetor))
