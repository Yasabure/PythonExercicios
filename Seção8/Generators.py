"""
Generators

- Tuple comprehension são chamadas de Generators

nomes = ['Carlos', 'Camille','Carla','Cassimiro','Cristina']

print(all([nome[0] == 'C' for nome in nomes]))
#Poderiamos fazer isso utilizando Generators

nomes = ['Carlos', 'Camille','Carla','Cassimiro','Cristina']

print(all(nome[0] == 'C' for nome in nomes))
#Isso não é list comprehension por não ter '[]'
#Entre o Generators e o List comprehension, o melhor é o Generators. Pq?
#Pq assim como Filter ou map, eles são objetos e para ver o seu conteudo é necessario converter o resultado
#Que logo é apagado após a primeira olhada, levando em consideração a memória, ela se destaca

#Qual é a utilidade de Getsizeof() -> retorna A quantidade de Mémoria do elemento passado com parâmetro

print(getsizeof('Geek'))
print(getsizeof('leonardo'))

#Mostra quantos bytes a string está ocupando em memória e ela é equivalente ao seu tamanho

from sys import getsizeof

#Gerando uma lista de elementos com list comprehension

list_com = getsizeof([x * 10 for x in range(1000)])

#Gerando uma lista de elementos com Set comprehension

set_com = getsizeof({x * 10 for x in range(1000)})

#Gerando uma lista de elementos com Dictionary comprehension

dic_com = getsizeof({x: x * 10 for x in range(1000)})

#Gerando uma lista de elementos com Generators

gen = getsizeof(x * 10 for x in range(1000))

print(f'Para Fazermos a mesma Tarefa Gastamos: List:{list_com}, Set:{set_com}, Dic:{dic_com}, Gen:{gen}')
"""

gen = (x * 10 for x in range(1001))
print(gen)
print(type(gen))

for n in gen:
    print(n)





