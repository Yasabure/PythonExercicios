import numpy as np 
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
soma = [0, 0, 0]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe o Valor da Matriz{l + 1}/{c + 1}: '))
        if c == 0:
            soma[c] += matriz[l][c]
        elif c == 1:
            soma[c] += matriz[l][c]
        elif c == 2:
            soma[c] += matriz[l][c]
for values in matriz:
    print(values)

soma1 = np.array(soma)
print(soma1)

