def diagonal_secundaria(matriz: list) -> list:
    m = 0
    d = 2
    soma = 0
    for l in range(0, 3):
        for c in range(0,3):
            if l == m and c == d:
                soma += matriz[l][c]
        m += 1
        d -= 1
    
    print(soma)

diagonal_secundaria([[1,2,3],[4,5,6],[7,8,9]])