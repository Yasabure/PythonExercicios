"""
lambda x: x -3 * 2
conta = lambda x: (x -3) * 2
print(conta(5))
"""

def pau(a,b,c):
    return lambda x: x + a * b + c

teste = pau(3,3,3)
print(teste(1)) #Com valores já definidos

#Com valores indefinidos

print(pau(1,2,3)(3))
 
#Ordenar Pelo Sobrenome

autores = ['Isac Newton', 'Tourindo P. Porra', 'Comi a Mãe', 'Voce e. Preto']

autores.sort(key=lambda sobrenome: sobrenome.split('')[-1].lower())

#Split(' ') Transforma o nome em uma lista, não separando as letras, mas sim as partes dos nomes(Nome, nome do meio e sobrenome)
#[-1] Pega o ultimo elemento
#.Lower() transforma o nome em minusculo
