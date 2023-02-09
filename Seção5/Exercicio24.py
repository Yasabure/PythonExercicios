altura_alunos = dict()
 
for n in range(1, 6):
    n = int(input('Número do aluno: '))
    altura_alunos[f'Aluno {n}'] = float(input(f'Altura do aluno {n}: '))
 
max = max(altura_alunos.values())
min = min(altura_alunos.values())
lista_max = list()
lista_min = list()
 
for key, values in altura_alunos.items():
    if values == max:
        lista_max.append(key)
    if values == min:
        lista_min.append(key)
 
print(f'A maior altura é {max}, cujo código do aluno é:', end=' ')
for valores in lista_max:
    print(f'{valores}', end=', ')
 
print(f'A menor altura é {min}, cujo código do aluno é:', end=' ')
for valores in lista_min:
    print(f'{valores}', end=', ')