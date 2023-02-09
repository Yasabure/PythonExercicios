matrizaA = [[1, 2, 3], [4,5,6], [7,8,9]]
matrizB= [[0, 0, 0], [0,0,0], [0,0,0]]

for l in range(0, 3):
    for c in range(0, 3):
        matrizB[l][c] = matrizaA[l][c] ** 2

for values in matrizB:
    print(values)
