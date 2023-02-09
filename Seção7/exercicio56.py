def somamatriz7x6(matriz: list, n: int) -> list and int:
    soma = 0
    a = 2
    if n > 6 and n < 0:
        print(f'Linha Não cumpre os requisitos')
    if soma != 42:
        if len(matriz) == 7:
            for r in range(0, 7):
                if len(matriz[r]) == 6:
                    soma += 6
        if soma != 42:
            matriz = list(input(f'Lista Não Cumpre Os Requisitos'))
    soma = 0
    for c in range(0, 6):
        soma += matriz[n + 1][c]
    print(f'A Soma Da Linha {n} é {soma}')


somamatriz7x6([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [
              1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]], 3)
