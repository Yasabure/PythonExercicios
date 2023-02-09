from itertools import count


numeros = [1,2,3,4,5,6]
"""
print([num * 10 for num in numeros])
print([num * 2 if num % 2 == 0 else num / 2 for num in numeros])
print([num for num in numeros if num % 2 == 0])
print([num for num in numeros if num % 2 != 0])
def comprar_carro(valor: float, salario: float):
    analise = ['Compre' if valor /24 < salario / 100 * 10 else 'Não Compre']
    return analise
print(comprar_carro(50.000, 23.000))
"""
sexo = ['f','f','f','m','m','f','m','f','m']
c= 0
ab = [sex for sex in sexo if sex == 'f'] + [sex for sex in sexo if sex == 'm']
print(ab)

