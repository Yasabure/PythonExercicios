def diagonal_principal(matriz: list) -> list:
    m = 0
    soma = 0
    for l in range(0, 3):
        for c in range(0,3):
            if l == m and c == m:
                soma += matriz[l][c]
        m += 1
    
    print(soma)

diagonal_principal([[1,2,3],[4,5,6],[7,8,9]])
