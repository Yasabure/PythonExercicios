#entradas
n1 = int(input("Informe um Valor: "))
#processamento
if n1 % 2 ==0 :
    if n1 > 0:
        print("O Número {0} é Par e Positivo".format(n1))
    else:
        print("O Número {0} é par e negativo".format(n1))  
else:
     if n1 > 0:
         print("O Número {0} é Impar e Positivo".format(n1))   
     else:
        print("O Número {0} é Impar e Negativo".format(n1))

