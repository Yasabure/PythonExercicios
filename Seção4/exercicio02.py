vetor1 = []
vetor2 = []
soma = []

for i in range (1, 10):
    num1 = int(input("Informe o Primeiro valor: "))
    vetor1.append(num1)
    num2 = int(input("Informe o Segundo valor: "))
    vetor2.append(num2)
    soma.append(num1 + num2)
for n in soma:
    print (n)