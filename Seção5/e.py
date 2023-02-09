
vetor = list()
n = int(input(f'Informe Um valor Positivo: '))
while n < 0:
    n = 0
    print('O Número Informado Não cumpre os Requisitos')
    n = int(input(f'Informe Um valor Positivo: '))
for r in range(n):
    if len(vetor) < 2:
         vetor.insert(len(vetor), 1)
    elif r >= 2:
        for i in range(len(vetor) -1):
         vetor.append(vetor[i] + vetor[i + 1] ) 
        for c in range(len(vetor) - r):
            vetor.pop(1)
        vetor.append(1) 
    print(vetor) 