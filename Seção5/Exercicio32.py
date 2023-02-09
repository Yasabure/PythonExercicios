x = []
y = []
soma = []
produto = []
diferenca = []
intersecao = []
uniao = []
for r in range(1,6):
    valor1 = int(input(f'Informe o Valor de X {r}/5: '))
    x.append(valor1)
    valor2 = int(input(f'Informe o Valor de Y {r}/5: '))
    y.append(valor2)
    soma.append(valor1 + valor2)
    produto.append(valor1 * valor2)
uniao.extend(x)
for valores in x:
    if valores in y:
        intersecao.append(valores)
    else:
        diferenca.append(valores)
for valores in y:
    if valores not in x:
        uniao.append(valores)

print(f' Soma: {soma}')
print(f' Produto: {produto}')
print(f' Diferença {diferenca}')
print(f' interseção: {intersecao}')
print(f' união: {uniao}')

      

