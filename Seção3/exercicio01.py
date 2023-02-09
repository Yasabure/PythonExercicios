maior = 0
valor = int(input("Informe um valor: "))
while valor != 0 :
    if valor > maior:
        maior = valor 
    valor = int(input("Informe um valor: "))
print("Maior Valor {0}".format(maior))