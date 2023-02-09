vetor = []
for i in range(1, 11):
    valor = int(input(f'Digite o {i}º valor inteiro do vetor: '))
    vetor.append(valor)
 
multiplos = 0
for valor in vetor:
    for divisor in range(2, valor):
        if valor % divisor == 0:
            multiplos += 1
    if multiplos == 0 and valor != 1:
        print(f'O número {valor} é primo e está na posição {vetor.index(valor)}')
    multiplos = 0



