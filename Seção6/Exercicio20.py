matriz = [[0, 0,0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
soma = [0, 0, 0, 0, 0]
for l in range(0, 3):
    for c in range(0, 6):
        matriz[l][c] = (int(input(f'Informe O valor Da Matriz {l + 1}/{c + 1}: ')))
        if (c + 1) % 2 != 0:
            soma[0] += matriz[l][c]
        if c + 1 == 2 or c + 1 == 4:
            soma[1] += matriz[l][c]
        if c + 1 == 1 or c + 1 == 2:
            soma[l+2] += matriz[l][c]
        if c + 1 == 6:
            matriz[l][c] = soma[l + 2]
print(f'Valor de Todas as Colunas Impares {soma[0]}')
print(f'Média aritimética dos elementos da segunda e quarta coluna: {soma[1] / 6}')
for values in matriz:
    print(values)

