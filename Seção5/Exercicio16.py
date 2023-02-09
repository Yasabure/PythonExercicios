vetor = []
for r in range(5):
    valor = int(input("Informe Um valor: "))
    vetor.append(valor)
c = int(input("Informe o Código: "))
if c != 0:
    if c == 1:
        print(vetor)
    if c == 2:
        vetor.reverse()
        print(vetor)
    else:
        print("Código Invalido")