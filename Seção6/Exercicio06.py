matriz1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matriz2 = [[2, 3, 4, 5], [1, 2, 3, 9], [15, -2, -6, 0], [32, 11, 44, 15]]
matriz3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0,4):
    for c in range (0,4):
        if matriz1[l][c] > matriz2[l][c]:
            matriz3[l][c] = matriz1[l][c]
        else:
            matriz3[l][c] = matriz2[l][c]
 
for valores in matriz3:
     print(valores)