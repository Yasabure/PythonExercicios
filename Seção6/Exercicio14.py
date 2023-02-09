import random
m = 0
p = 0
matriz = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
for l in range(0 , 5):
    for c in range(0, 5):
        matriz[l][c] = random.randrange(0, 99)
        for r in range(0, 5):
             m += matriz[r].count(matriz[l][c])
             while m > 1:
                  matriz[l][c] = random.randrange(0, 99)
                  for k in range(0, 5):
                     p += matriz[k].count(matriz[l][c])
                     if p == 1:
                          m = 0
                          p = 0
for values in matriz:
    print(values)            