notas = [[8, 10, 7], [9, 5, 3], [8, 9, 10], [7, 7, 8], [3, 0, 3],
         [8, 1, 1], [9, 7, 8], [5, 9, 8], [8, 7, 10], [9, 7, 5]]
menor = 999
prova = 0
pior = 0
pior2 = 0
pior3 = 0
for l in range(0, 10):
    for c in range(0, 3):
        if notas[l][c] < menor:
            menor = notas[l][c]
            prova = c
    if prova == 0:
        pior += 1
    elif prova == 1:
        pior2 += 1
    elif prova == 2:
        pior3 += 1
    menor = 999

print(f'Total De Alunos que tiveram Suas Piores notas na Prova')
print(f'         Prova 1          Prova 2          Prova3')
print(f'            {pior}                {pior2}                {pior3}   ')
