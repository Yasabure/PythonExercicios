v = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
variancia = 0 
soma = sum(v)
for j in v:
    variancia += (j - (soma / len (v))) ** 2
s = variancia / (len(v) - 1)
d = s ** 0.5
print(f'Desvio padrão: {d:.4f}')

