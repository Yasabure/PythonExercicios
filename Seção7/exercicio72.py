def mult_vetor(v1: list, v2: list):
    v3 = []
    menor = 0
    maior = 0
    if len(v1) > len(v2):
        maior = len(v1)
        menor = len(v2)
    else:
        maior = len(v2)
        menor = len(v1)

    for r in range(0, menor):
        v3.append(v1[r] * v2[r])
    for i in range(menor, maior):
        if maior == len(v1):
            v3.append(v1[i])
        else:
            v3.append(v2[i])
    print(v3)

mult_vetor([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9,0])
