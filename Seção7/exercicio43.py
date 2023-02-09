import random
def vetor_aleatorio(vetor: int and list ) -> int and list:
    for r in range(0,10):
        if len(vetor) < 10:
             vetor.append(random.randrange(100))
             while vetor.count(vetor[len(vetor) - 1]) > 1:
                 vetor[len(vetor)]= random.randrange(100) 




    print(vetor)

vetor_aleatorio([1, 2, 3])

    