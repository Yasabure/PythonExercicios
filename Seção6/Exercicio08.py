matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = 0
soma = 0    
for l in range(0, 3):
    for c in range(m, 3):
        if l == c:
           m += 1
        if l != c and l < 2:
            soma = soma + matriz[l][c]
        if m == 3:
           l = 2
print(soma)

