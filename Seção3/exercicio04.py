soma = 0
maior = -999
menor = 999
for n in range(1,11):
    valor = int(input("Informe um valor: "))
    if valor > 0:
       if valor > maior:
           maior = valor
       if valor < menor:
           menor = valor
       soma = valor + soma
    else:
        valor = int(input("Informe um valor"))  
media = soma / 10
print("O Maior Valor é : {0}".format(maior))
print("O Menor Valor é : {0}".format(menor))
print("A Média Dos valores é: {0}".format(media))

