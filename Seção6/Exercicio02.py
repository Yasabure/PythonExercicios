matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
c = 0
for l in range(0,5):
    for co in range(0, 1):
        matriz[l][c] = 1
        c += 1
for values in matriz:
    print(values)
