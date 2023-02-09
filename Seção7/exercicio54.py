def somamatriz4x4(matriz: list) -> list:
    soma = 0
    if soma != 16:
        if len(matriz) == 4:
            for r in range(0, 4):
                if len(matriz[r]) == 4:
                    soma += 4
        if soma != 16:
            matriz = list(input(f'Lista Não Cumpre Os Requisitos'))
    soma = 0
    for c in range(0, len(matriz)):
        for d in range(0, len(matriz)):
            soma += matriz[c][d]

    print(soma)


somamatriz4x4([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1,1]])
