matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = l * c
for v in matriz:
    print(v)