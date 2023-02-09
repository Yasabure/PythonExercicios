import random
matriz = []
maior = -999
soma = 0
for l in range(0, 20):
    matriz.append([])
    for c in range(0, 20):
        matriz[l].append(random.randrange(0,99))

for l in range(0, 20):
    for c in range(0, 20):
        if c > 2:
            for r in range(0, 4):
                if soma == 0:
                    soma = matriz[l][c - r]
                else:     
                    soma = soma * matriz[l][c - r]
            if soma > maior:
                maior = soma
            soma = 0
        if c < 17:
            for r in range(0, 4):
                if soma == 0:
                    soma = matriz[l][c + r]
                else:
                    soma = soma * matriz[l][c + r]
            if soma > maior:
                maior = soma
            soma = 0
        if l < 17:
            for r in range(0, 4):
                if soma == 0:
                    soma = matriz[l + r][c]
                else:
                    soma = soma * matriz[l + r][c]
            if soma > maior:
                    maior = soma
            soma = 0
        if l > 2:
            for r in range(0, 4):
                if soma == 0:
                    soma = matriz[l - r][c]
                else:
                    soma = soma * matriz[l - r][c]
            if soma > maior:
                maior = soma
            soma = 0
        if l < 17 and c < 17:
            for r in range(0, 4):
                if soma == 0:
                    soma = matriz[l + r][c + r]
                else:
                    soma = soma * matriz[l + r][c + r] 
            if soma > maior:
                maior = soma
            soma = 0
        if l < 17 and c < 17:
            for r in range(0, 4):
                if soma == 0:
                    soma = matriz[l - r][c - r] 
                else:
                    soma = soma * matriz[l - r][c - r]    
            if soma > maior:
                maior = soma
            soma = 0

for values in matriz:
    print(values)

print(maior)