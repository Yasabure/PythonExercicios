vetor = []

for r in range(1, 11):
    valor = int(input(f'informe Um valor {r}/10: '))
    while valor in vetor:
        print('Informe Um Valor Não informado antes')
        valor = int(input(f'informe Um valor {r}/10: '))
    vetor.append(valor)
print(vetor)