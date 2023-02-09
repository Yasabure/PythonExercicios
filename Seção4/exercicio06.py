vetor = []
cdg = int(input("Informe o Código: "))
if cdg > 0:
    for i in range(0,5):
        num=int(input("Informe um valor: "))
        vetor.append(num)
    if cdg == 1:
        for i in vetor:
            print(i)
    if cdg == 2:
        vetor.reverse()
        for i in vetor:
            print(i)