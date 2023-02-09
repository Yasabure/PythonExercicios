from itertools import count


def soma2_vetores(vetor1: list, vetor2: list) -> list:
    soma = 0
    vetor3 = []
    for r in range(0, len(vetor1)):
        for c in range(0, len(vetor2)):
            soma+= 1
    if soma != 100:
        return ('Os Vetores Não Cumprem os requisitos(10 Valores)')
    for i in range(0, len(vetor1)):
        vetor3.append(vetor1[i])
    for c in range(0,len(vetor2)):
        if vetor3.count(vetor2[c]) == 0:
            vetor3.append(vetor2[c])
    
    print(vetor3)

soma2_vetores([1, 2, 3, 4, 5, 6, 7, 8, 9,10],[11, 12, 13, 14, 15, 16, 17, 18, 19,20])
    