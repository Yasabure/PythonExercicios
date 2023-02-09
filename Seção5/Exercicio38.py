vetor = list()

for r in range(1, 11):
    valor = int(input(f'Informe o Valor {r}/10: '))
    while vetor.count(valor) > 0:
        print('Não é Permitido Valores Repetidos')
        valor = int(input(f'Informe o Valor {r}/10: '))
    if r > 0:
        vetor.append(valor)
        vetor.sort()
    else:
        vetor.append(valor)
    print(vetor)