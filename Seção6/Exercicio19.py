notas = [[1, 5, 3, 0], [2, 6, 2, 0], [3, 4, 3, 0], [4, 3, 2, 0], [5, 7, 3, 0]]
soma = 0
maior = 0
for l in range(0, 5):
    for c in range(1, 4):
        if c == 3:
            if notas[l][c] == 0:
                notas[l][c] = notas[l][1] + notas[l][2]
                soma += notas[l][c]
                if notas[l][c] > notas[l- 1][c]:
                    maior = l 
print(f'Id    M/Prova    M/Trabalho')
for r in range(0,  5):
    print(f'{notas[r][0]}        {notas[r][1]}            {notas[r][2]}'),
print(f'Aluno Com Maior nota: {maior + 1}')
print("Media Das Notas Finais: {0}".format(soma / 5))
