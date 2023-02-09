from re import A


def separar(vetor: int and list)-> int and list:
    par = []
    impar = []
    for r in vetor:
        if r % 2 == 0:
            par.append(r)
        else:
            impar.append(r)
    print(f'Números Pares: {par}Impares {impar}')

separar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])


    

