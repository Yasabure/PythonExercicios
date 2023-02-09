matriz = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
maior = -999
for l in range(0, 4):
    for c in range(0 , 4):
        matriz[l][c] = int(input(f'Informe um Valor para [{l} {c}]: '))
        if matriz[l][c] > maior:
            maior = matriz[l][c]
            localizacao = l, c
for r in matriz:
    print(r)
print(f'O Maior está localizado em {localizacao} ')