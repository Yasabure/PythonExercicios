matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for r in range(0, 3):
    for l in range(0, 3):
        for c in range(0, 3):
            if c == r:
                matriz1[r][l] = matriz[l][c]
for values in matriz1:
    print(values)