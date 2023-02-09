def matriz_quadrada(matriz: list) -> list:
    matriz1 = []
    for r in range(0, len(matriz)):
        if len(matriz) != len(matriz[r]):
              print(f'Matriz Não é uma Matriz Quadrada')
              matriz = list(input(f' Informe Uma Matriz Quadrada: '))
    for c in range(0, len(matriz)):
        matriz1.append([])
        for d in range(0, len(matriz)):
            matriz1[c].append(matriz[d][c])

    print(matriz1)
    

matriz_quadrada([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

    