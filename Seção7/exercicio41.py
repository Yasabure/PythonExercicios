def vetor_maior(vetor: int and list ) -> int and list:
    maior = -999
    for r in vetor:
        if r > maior:
            maior = r

    return maior 

print(vetor_maior([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
