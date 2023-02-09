"""
Map

Utilizamos para mapear os valores da função

import math

def area(r):
    #Calcule a area de um circulo com raio 'r'
    return math.pi * (r ** 2)

#print(area(2))

raios = [2,5,7.1,0.3,10,44]
areas = []
areas =  map(area, raios)
#Map recebe duas entradas, primeiro a função e segundo um interavel

print(areas) #Aqui ele se porta como um map object e não apresenta nenhum dado
print(list(areas)) # Aqui ele se porta como uma lista e utiliza a função mencionada em cada valor

#Com lambda agora

print(list(map(lambda r: math.pi * (r ** 2), raios)))
# Obs: Após utilizar a função map() dps da primeira utilização do resultado (Transformando em Lista) ele zera
"""

Cidades = [('Berlim', 29), ('Cairo', 36), ('São Paulo', 19)]

c_to_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_to_f, Cidades)))