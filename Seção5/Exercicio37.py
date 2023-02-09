vetor = list(range (1, 12))
vetora = []
crescente = list()
decrescente = list()
import random
random.shuffle(vetor)
vetor.sort()
for r in range(5):
    crescente.append(vetor[r])
vetor.sort(reverse=True)
for r in range(6):
    decrescente.append(vetor[r])
vetora = crescente + decrescente 
print(vetora)
