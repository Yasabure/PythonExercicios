a = []
b = []
c = []
indice = 0
for r in range(10):
    valora = int(input("Informe O Valor De A {0}/10: ".format(indice + 1)))
    a.append(valora)
    valorb = int(input("Informe O Valor De B {0}/10: ".format(indice + 1)))
    b.append(valorb)
    indice = indice + 1
    c.append(valora - valorb)
print(c)
