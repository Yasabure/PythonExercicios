vetor = []

for r in range(1, 16):
    valor = int(input(f'Informe um Valor {r}/15: '))
    if valor != 0:
      vetor.append(valor)        
print(vetor)
if 0 in vetor:
    print('há Zero')
else:
    print('não há zero')

# ou 
v1 = [1, 2, 0, 0, 0, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for i in range(v1.count(0)):
        v1.remove(0)
print(v1)