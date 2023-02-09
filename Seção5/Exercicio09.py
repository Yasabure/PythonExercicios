vetor = []
for r in range(6):
    par = int(input("Informe um valor Par: "))
    while par % 2 != 0:
        print('O valor informado Não é Par')
        par = int(input("Informe um valor Par: "))
    vetor.append(par)
vetor.reverse()
print(vetor)