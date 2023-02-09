matriz = [[24, 30], [35, 40]]
matriz1 = [[50, 70], [100, 200]]
matriz2 = [[0, 0], [0, 0]]
print('a = Somar As Matrizes')
print('b = subtrair As Matrizes')
print('c = Adicionar Uma constante nas Matrizes')
print('d = Imprimir as Matrizes')
r = input(f' Informe o que deseja fazer com as matrizes: ')

if r == 'c':
    constante = float(input(f'Informe o valor da Constante:  '))
for l in range(0, 2):
    for c in range(0, 2):
        if r == 'a':
            matriz2[l][c] = matriz[l][c] + matriz1[l][c]
        elif r == 'b':
            matriz2[l][c] = matriz[l][c] - matriz1[l][c]
        elif r == 'c':
            matriz[l][c] += constante
            matriz1[l][c] += constante
        elif r == 'd':
            print('Primeira Matriz')
            for values in matriz:
                print(values)
            print('Segunda Matriz')
            for valores in matriz1:
                print(valores)
            [l] = 2
            [c] = 2
print(matriz2)
print(matriz)
print(matriz1)