import numpy 
def volume_esfera(r):
    return 4/3 * numpy.pi * (r**3)

a = float(input('Informe o Raio Da Esfera: '))

print(f'O volume da esfera é {volume_esfera(a)}')

