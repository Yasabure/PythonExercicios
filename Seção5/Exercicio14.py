vetor = []
a = []
for r in range(10):
    valor = int(input("Informe Um valor: "))
    vetor.append(valor)

for valor  in vetor:
    if valor not in a:
        quantidade = vetor.count(valor)
        if quantidade > 1:
            print(f"Existem {quantidade} valores no vetor")
            a.append(valor)