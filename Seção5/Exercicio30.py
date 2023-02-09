vetor = []
vetor1 = []
vetor2 = []
for r in range(1, 11):
    valor1 = int(input(f'Informe o Valor Do Vetor1 {r}/10: '))
    vetor1.append(valor1)
    valor2 = int(input(f'Informe o Valor Do Vetor2 {r}/10: '))
    vetor2.append(valor2)
for valores in vetor1:
    if valores in vetor2:
      vetor.append(valores)
print(vetor)