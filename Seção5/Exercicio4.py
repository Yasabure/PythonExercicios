vetor = []
for r in range(8):
    valor = int(input("Informe um valor: "))
    vetor.append(valor)

x = int(input("Informe o Valor de X: "))
while x > 9 and x < 0:
    print("O Valor deve ser Maior que 0 e Menor que 9")
    x = int(input("Informe o Valor de X: "))
y = int(input("Informe o Valor de Y: "))
while y > 9 and y < 0:
    print("O Valor deve ser Maior que 0 e Menor que 9")
    y = int(input("Informe o Valor de Y: "))

soma = vetor[x] + vetor[y]
print(soma)
