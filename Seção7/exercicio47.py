def matriz_maior10(matriz: list) -> list:
    maiorque10 = []
    for l in range(0, 4):
        for c in range(0, 4):
            if matriz[l][c] > 10:
                maiorque10.append(matriz[l][c])
    print(maiorque10)

matriz_maior10([[1, 2, 3, 4],[5,6,7,8],[9, 10, 11, 12],[13, 14, 15, 16]])

