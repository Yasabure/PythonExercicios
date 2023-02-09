"""
A função Reduce(), funciona da seguinte forma: 
Passo 1: res = f(a1, a2) # Aplica a função nos dois primeiros elementos e guarda o res
passo 2: res = f(r1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento

Isso até o final.
..
.
.
passo n: resn= f(resn, an)
ou seja em cada passo ela aplica a função passando o primeiro argumento como resultado da aplicação anterior
"""

from functools import reduce

dados = [2,3,4,5,7,11,13,17,19,23,29]
#Para utilizar o reduce() nós precisamos de uma função que receba dois parametros

multi = lambda x, y: x * y

res= reduce(multi,dados)
print(res)