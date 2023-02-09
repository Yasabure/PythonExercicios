matriz = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
m = 0
for l in range(0, 3):
    for c in range(0, 3):
        if c > m:
            matriz[l][c] = 0
    m += 1
for values in matriz:
    print(values)