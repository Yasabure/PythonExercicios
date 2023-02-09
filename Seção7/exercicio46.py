from msilib.schema import Media


def funcoes_vetor(vetor: list) -> list:
    print(vetor)
    vetor.reverse()
    print(vetor)
    print(sum(vetor)/len(vetor))

funcoes_vetor([2, 3, 3, 5, 7, 10])