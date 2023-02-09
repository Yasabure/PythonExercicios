"""
Reversed

obs: Reversed e Reverse() São Diferentes
Reversed() Reverte qualquer interavel, seja ele interavel ou string
"""

for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')

print(''.join(list(reversed('Geek University'))))

print('Geek university'[::-1])

#Range ao contrario

for n in range(9,-1, -1):
    print(n)