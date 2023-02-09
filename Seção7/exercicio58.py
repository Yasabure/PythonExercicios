def verficar_matriz_quadrada(matriz: list) -> list:
    soma = 0
    if soma != len(matriz):
        for r in range(0, len(matriz)):
                if len(matriz[r]) == len(matriz):
                    soma+= 1
        if soma != len(matriz):
            matriz = list(input(f'Lista Não Cumpre Os Requisitos'))
    if soma == len(matriz):
         return soma
def soma_matrizes(matriz1: list, matriz2: list) -> list:
    a = verficar_matriz_quadrada(matriz1)
    soma = 0
    b = verficar_matriz_quadrada(matriz2)
    c = []
    if a == b:
        for r in range(0, a):
            c.append([])
            for e in range(0, a):
                for h in range(0, b):
                     soma +=matriz1[r][h] * matriz2[h][e]
                c[r].append(soma)
                print(soma)
                soma = 0
    print(f'O Resultado Da Primeira Matriz  * A Segunda é: {c}')

soma_matrizes([[-1,3],[4, 2]], [[1, 2],[3,4]])

