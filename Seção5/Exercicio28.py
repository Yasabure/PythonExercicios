v = []
v1 = []
v2 = []
indice = 1
for r in range(1, 11):
    valor = int(input('Informe um valor {0}/10: '.format(indice)))
    v.append(valor)
    indice += 1
    if valor % 2 == 0:
        v1.append(valor)
    else:
        v2.append(valor)

print(f'Os Elementos utilizados de V1 foram : {len(v1)}')
print(f'Os Elementos utilizados de V2 foram : {len(v2)}')