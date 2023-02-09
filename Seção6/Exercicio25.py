matriz = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
a = 2
b = 1
v = 0
g = 0
play1 = input('Qual Será seu Simbolo O/X?: ')
if play1 == 'O':
    play2 = 'X'
else:
    play2 = 'O'

for values in matriz:
    v += values.count(-1)

while v != 0:
    print(f'     1   2   3')
    for values in matriz:
        print(f'{b}  {values}')
        b += 1
    b = 1
    l = int(input(f'Informe Em Qual Linha  Deseja Jogar: '))
    c = int(input(f'Informe Em Qual Coluna Deseja Jogar: '))
    if matriz[l - 1][c - 1] == -1:
        if v % 2 == 0:
            matriz[l - 1][c - 1] = play2
        else:
            matriz[l - 1][c - 1] = play1
    else:
        while matriz[l - 1][c - 1] != -1:
            print('Local jogado já se encontra Com um Movimento')
            l = int(input(f'Informe Em Qual Linha  Deseja Jogar: '))
            c = int(input(f'Informe Em Qual Coluna Deseja Jogar: '))
            if v % 2 == 0:
                matriz[l - 1][c - 1] = play2
            else:
                matriz[l - 1][c - 1] = play1
    v -= 1
    for l in range(0, 3):
        for c in range(0, 3):
            for r in range(0, 3):
                 if matriz[r][a] == play1:
                     g += 1
                     a -= 1
                     
                 if r == 2:   
                    a = 2  
                    if g == 3:
                        if matriz[r][a] == play1:
                            print('Player 1 Ganhou')
                            v = 0 
                        else:
                            print('Player 2 Ganhou')
                            v = 0
                    else:
                        g = 0
            for r in range(0, 3):
                 if matriz[r][a] == play2:
                     g += 1
                     a -= 1
                     
                 if r == 2:   
                    a = 2  
                    if g == 3:
                        if matriz[r][a] == play2:
                            print('Player 2 Ganhou')
                            v = 0 
                            g = 0
                        else:
                            print('Player 1 Ganhou')
                            v = 0
                            g = 0
                    else:
                        g = 0
            for r in range(0, 3):
                 if matriz[l][r] == play1:
                     g +=1
                 if r == 2:
                     if g == 3:
                         if matriz[l][r] == play1:
                             print('Player 1 Ganhou')
                             v = 0 
                             g = 0
                         else:
                             print('Player 2 Ganhou')
                             v = 0
                             g = 0
                     else:
                        g = 0
            for r in range(0, 3):
                 if matriz[l][r] == play2:
                     g +=1
                 if r == 2:
                     if g == 3:
                         if matriz[l][r] == play2:
                             print('Player 2 Ganhou')
                             v = 0 
                             g = 0
                         else:
                             print('Player 1 Ganhou')
                             v = 0
                             g = 0
                     else:
                        g = 0
            for r in range(0, 3):
                 if matriz[r][r] == play1:
                     g +=1
                 if r == 2:
                     if g == 3:
                         if matriz[r][r] == play1:
                             print('Player 1 Ganhou')
                             v = 0 
                             g = 0
                         else:
                             print('Player 2 Ganhou')
                             v = 0
                             g = 0
                     else:
                        g = 0
            for r in range(0, 3):
                 if matriz[r][r] == play2:
                     g +=1
                 if r == 2:
                     if g == 3:
                         if matriz[r][r] == play2:
                             print('Player 2 Ganhou')
                             v = 0 
                             g = 0
                         else:
                             print('Player 1 Ganhou')
                             v = 0
                             g = 0
                     else:
                        g = 0
            for r in range(0, 3):
                 if matriz[r][c] == play1:
                     g +=1
                 if r == 2:
                     if g == 3:
                         if matriz[r][c] == play1:
                             print('Player 1 Ganhou')
                             v = 0 
                             g = 0
                         else:
                             print('Player 2 Ganhou')
                             v = 0
                             g = 0
                     else:
                        g = 0
            for r in range(0, 3):
                 if matriz[r][c] == play2:
                     g +=1
                 if r == 2:
                     if g == 3:
                         if matriz[r][c] == play2:
                             print('Player 2 Ganhou')
                             v = 0 
                             g = 0
                         else:
                             print('Player 1 Ganhou')
                             v = 0
                             g = 0
                     else:
                        g = 0
           
    if v == 0:
        revanche = input(f'Deseja Revanche? s/n: ')
        if revanche != 'n':
            for l in range(0,3):
                for c in range(0, 3):
                    matriz[l][c] = -1
            v = 9