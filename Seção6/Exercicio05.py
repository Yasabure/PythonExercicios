matriz = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
valor = int(input(f'Informe o Valor A Ser procurado: '))
valor1 = 0
loca = list()
l = 0
c = 0
for values in matriz:
    for valores in values:
        if valores == valor:
            valor1 += 1
            loca = l , c
        c += 1
    l += 1
    c = 0
if valor1 != 0:
    print(f'Valor Encontrado em {loca}')
else:
    print(f'Valor não Encontrado')
        