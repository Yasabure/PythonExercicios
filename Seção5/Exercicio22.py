a = []
b = []
c = []
i = 0
indice = 0
for r in range(10):
    valora = int(input("Informe O Valor De A {0}/10: ".format(indice + 1)))
    a.append(valora)
    c.insert(i, valora)
    valorb = int(input("Informe O Valor De B {0}/10: ".format(indice + 1)))
    b.append(valorb)
    c.insert(i + 1, valorb)
    indice = indice + 1
    i = i + 1
print(c)
