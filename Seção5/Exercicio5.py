vetor = [9]
p = 0
for r in range(10):
    valor = int(input("Informe um Valor: "))
    vetor.append(valor)
    if valor % 2 == 0:
        p = p + 1
print("O Vetor Possui {0} Números Pares".format(p))