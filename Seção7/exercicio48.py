def soma_diagonalprincipal(matriz: list) -> list:
    soma = 0
    r = 0
    m = 1
    for l in range(0, 3):
        for c in range(0, 3):
            if l >=r and c >= m:
                soma+=matriz[l][c]
                if c != 0:
                    m +=1
        r +=1
        m = r + 1



    print(soma)

soma_diagonalprincipal([[1,2,3],[4,5,6],[7,8,9]])

            
            

            