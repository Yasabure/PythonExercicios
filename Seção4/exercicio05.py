vetor = []
maiores_50 = False
for i in range(1,11):
    num1=int(input("Digite um valor: "))
    vetor.append(num1)
for i in vetor: 
    if i > 50:         
        print("Valor: {0} Maior que 50 Na posição {1}".format(num1, vetor.index(i)))
        maiores_50 = True
if maiores_50 == False:
    print("Não há números maiores que 50")
