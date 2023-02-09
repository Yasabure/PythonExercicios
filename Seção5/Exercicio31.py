vetor = []
vetor1 = []
vetor2 = []
for r in range(1, 11):
    valor = int(input(f'Informe o Valor Do Vetor1 {r}/10: '))
    vetor1.append(valor)
    valor = int(input(f'Informe o Valor Do Vetor2 {r}/10: '))
    vetor2.append(valor)
vetor.extend(vetor1)
vetor.extend(vetor2)
s = set(vetor)
s = list(s)
print(s)
       
