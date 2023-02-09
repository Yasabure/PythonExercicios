gabarito = ['a', 'b', 'c', 'd', 'e','a', 'b', 'c', 'd', 'e']
matriz = [['a','a','c'], ['a','b','c'], ['a','c','c'], ['a','d','c'], ['a','e','c'], ['a','a','c'], ['a','b','c'], ['a','b','c'], ['a','b','c'], ['a','b','c']]
leo = 0
be = 0
le = 0 

r = 0
for l in range(0, 10):
    for c in range(0, 3):
        if matriz[l][c] == gabarito[r]:
            if c == 0:
                leo += 1
            if c == 1:
                be += 1
            if c == 2:
                le += 1
    r += 1
print(f'Prova De Setembro')
print(f' 22,  24,  39')
for values in matriz:
    print(values)
print(f'Taxa de Acerto')
print(f'  {leo}    {be}    {le}')
if (leo + be + le) / 3 < 7:
    print('   REPROVADOS')
else:
    print('   Aprovados')


            
                
