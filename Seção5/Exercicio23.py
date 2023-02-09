a = set({})
b = set({})
c = []
d = []
indice = 0
produto = 0
for r in range(5):
    valora = int(input("Informe um valor A {0}/5: ".format(indice + 1)))
    a.add(valora)
    c.append(valora)
    valorb = int(input("Informe um valor B {0}/5: ".format(indice + 1)))
    b.add(valorb)
    d.append(valorb)
    indice = indice + 1
    produto = produto + valora * valorb
print(c)
print(d)
print(produto)


