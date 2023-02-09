def somamatriz3x3(matriz: list) -> list:
    soma = 0
    a = 2
    if soma != 9:
        if len(matriz) == 3:
            for r in range(0, 3):
                if len(matriz[r]) == 3:
                    soma += 3
        if soma != 9:
            matriz = list(input(f'Lista Não Cumpre Os Requisitos'))
    soma = 0
    for c in range(0, len(matriz)):
        if c != 1:
             soma += matriz[c][a]
             a -= 2
        for d in range(0, len(matriz)):
            if d == c:
                soma += matriz[c][d]
    print(soma)

somamatriz3x3([[1,2,1],[4,1,6],[1,8,1]])