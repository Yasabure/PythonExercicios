"""
Any e All

all() -> Retorna True se todos os elementos iterável são verdadeiros ou ainda se o interável está vazio

print(all([0,1,2,3,4])) #Todos os números São verdadeiros? Não, pois o 0 é considerado falso 
print(all([1,2,3,4]))
print(all([]))
print(all(['Pirulito']))

nomes = ['Carlos', 'Camille','Carla','Cassimiro','Cristina']

print(all([nome[0] == 'C' for nome in nomes]))
# Checagem para ver se todos os nomes se inicial com a letra 'C'

print(all([letra for letra in 'eio' if letra in 'aeiou']))
#Obs um interavel vazio é dado como true, mas se convertido em 'bool' é false

print(all([num for num in [1,2,3,4,5,6,7,8] if num % 2 == 0]))


Any() -> Retorna True se qualquer elemento do interável for verdadeiro. Se o interavel estiver vazio é false
"""
print(any([num for num in [1,4,3,5,7] if num % 2 == 0]))

#Funciona da mesma forma que o 'All()'. porém há algumas mudanças como:
#Interavel vazio é dado como 'False'
#Retorna True se apenas um interavel atender os requisitos




