matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
maior10 = 0
maior = list ()
for l in range(0,4):
    for c in range(0, 4):
        matriz[l][c]= int(input(f'Informe um Valor Para [{l}, {c}]: '))
        if matriz[l][c] > 10:
            maior10 += 1
            maior.append(matriz[l][c])
print(f'Há {maior10} números maiores que 10, sendo eles {maior}')
