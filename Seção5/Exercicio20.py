vetor = []
impar = []
indice = 0
for r in range(10):
    valor = int(input("Informe um valor: "))
    while valor > 50 and valor < 0:
        print("Valor Acima ou Abaixo do Permitido")
        valor = int(input("Informe um valor: "))
    vetor.append(valor)
    if valor % 2 != 0:
        impar.append(valor)
while indice < len(impar):
     print(vetor[indice], impar[indice])
     indice = indice + 1
while indice < len(vetor):
    print(vetor[indice])
    indice = indice + 1
