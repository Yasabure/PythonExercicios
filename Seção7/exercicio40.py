def pares_vetor(vetor: list) -> list:
    lista = []
    for i in vetor:
        if i % 2 == 0:
            lista.append(i)
    
    print(lista)

pares_vetor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

