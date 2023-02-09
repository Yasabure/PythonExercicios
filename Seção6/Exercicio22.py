matriz = [[1, 2, 3], [4,5,6], [7,8,9]]
matriz1 = [[1, 2, 3], [4,5,6], [7,8,9]]
matriz2 = [[0, 0, 0], [0,0,0], [0,0,0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz2[l][c] = matriz[l][c]+ matriz1[l][c]

for values in matriz2:
    print(values)