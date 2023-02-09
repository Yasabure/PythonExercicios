gabarito = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']
matriz = [['a', 'b', 'a', 'c','d'], ['a', 'b', 'a', 'c','d'], ['a', 'b', 'a', 'c','d'], ['a', 'b', 'a', 'c','d'], ['a', 'b', 'a', 'c','d'], ['a', 'b', 'a', 'c','d'], ['a', 'b', 'a', 'c','d'], ['a', 'b', 'a', 'c','d'], ['a', 'b', 'a', 'c','d'], ['a', 'b', 'a', 'c','d']]
acertos1 = 0
acertos2 = 0
acertos3 = 0
acertos4 = 0
acertos5 = 0
r = 0
for l in range(0, 10):
    for c in range(0, 5):
        if matriz[l][c] == gabarito[r]:
            if c == 0:
                acertos1 += 1
            elif c == 1:
                acertos2 += 1
            elif c == 2:
                acertos3 += 1
            elif c == 3:
                acertos4 += 1
            elif c == 4:  
                acertos5 += 1      
    r += 1
print(f'Resultados: Aluno1: {acertos1}/10, Aluno2: {acertos2}/10, aluno3: {acertos3}/10, aluno4: {acertos4}/10, aluno5: {acertos5}/10')


