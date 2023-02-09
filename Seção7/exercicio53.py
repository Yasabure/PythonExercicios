def matrizidentidade(matriz: list) -> list:
    a = 0
    for r in range(0, len(matriz)):
        if len(matriz) != len(matriz[r]):
              print(f'Matriz Não é uma Matriz Quadrada')
              matriz = list(input(f' Informe A Matriz Corretamente: '))
    for c in range(0, len(matriz)):
        for d in range(0, len(matriz[c])):
            if c == d and matriz[c][d] == 1:
                a += 1
            if c != d:
                if matriz[c][d] == 0:
                     a += 1
    if a == len(matriz) * len(matriz[0]):
        print(f'Essa é uma matriz Identidade')
    else:
        print(f'Essa não é uma matriz identidade')
        print(a)

matrizidentidade([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]])


            

