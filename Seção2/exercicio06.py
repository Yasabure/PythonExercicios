#variaveis
valor_hora = 10.00
valor_hora_excedente = 20.00
e = 0
#entradas
c=int(input("Informe Seu Código: "))
n=float(input("Informe o Número de Horas trabalhadas: "))
#processamento
if n > 50:
    e = (n - 50) * valor_hora_excedente
    salario = (50 * valor_hora) + e 
    print("Salario Total R$:{0:.2f} ".format(salario))
    print("Extra:{0:.2f} ".format(e))
else:
    salario = (n * valor_hora)
    print("Sálario Total R$ {0:.2f}".format(salario))
    print("Sálario Excedente R$ {0:.2f}".format(e))