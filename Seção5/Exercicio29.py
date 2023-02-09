vetor = []
par = []
impar = []
for r in range(6):
    valor = int(input('Informe o Valor: '))
    vetor.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor) 
print(f'Números Pares Digitados: {par}')
print(f'Soma dos Números Pares: {sum(par)}')
print(f'Números Impares Digitados : {impar}')
print(f'(Quantidade de Números impares Digitados: {len(impar)}')

