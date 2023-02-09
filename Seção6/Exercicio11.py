matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = 2
soma = 0

for l in range(0,3):
    for c in range(0,3):
        if c == m:
            soma = matriz[l][c] + soma
            m = m - 1
print(soma)