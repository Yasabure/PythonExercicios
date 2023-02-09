a = []
b = []

valora = int(input('Informe o Valor A entre 1/9999: '))
while valora > 9999 or valora < 1:
    print('Valor Não Cumpre os Requisitos')
    valora = int(input('Informe Um Valor entre 1/9999: '))
valorb = int(input('Informe o Valor B de 1 A 9999: '))
while valorb > 9999 or valorb < 1:
    print('Valor Não Cumpre os Requisitos')
    valorb = int(input('Informe o Valor B de 1 A 9999: '))

a.append(valora // 1 % 10)
b.append(valorb // 1 % 10)
 
a.insert(0,valora // 10 % 10)
b.insert(0, valorb // 10 % 10)
 
a.insert(0, valora // 100 % 10)
b.insert(0, valorb // 100 % 10)

a.insert(0, valora // 1000 % 10)
b.insert(0, valorb // 1000 % 10)

indice = 3
somas = []
while indice >= 0:
    somas.append(a[indice] + b[indice])
    indice = indice - 1
indice = 0
if somas[3] > 9:
       somas.insert(4, 0)
for r in range(len(somas)):
   i = somas[indice]
   if i > 9:
       somas[indice] = somas[indice] - 10
       somas[indice + 1] = somas[indice + 1] + 1
   indice = indice + 1 
somas.reverse()  
print(f'O resultado é {somas}, ou {valora+ valorb}') 