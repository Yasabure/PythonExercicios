"""
Min E Max

Max() -> Retorna o maior valor em um interavel 
Min() -> Retorna O menor valor em um interavel

#Max em dicionario

dic = {'a': 12,  'b': 5}

print(max(dic)) #Aquiele retorna a chave que retem o maior valor
print(max(dic.values())) #Aqui ele Retorna o maior valor
"""



nomes = ['Alber', 'Jesus', 'Matias','Leonardo','Ana']
print(max(nomes)) #Retornara Ana. Quando Utilizamos Max com String ele vai pela ordem alfabética
print(min(nomes)) #Retornara Matias. Pois na ordem alfabética, O 'M' Vem depois de 'A, J, L'

print(max(nomes, key=len)) #Aqui Retornara com base No número de Caracteres 'Leonardo'
print(min(nomes, key=len)) #'Ana'

musicas = [
    {"Titulo" : "Vish", "tocou": 3},
    {"Titulo" : "Tarda", "tocou": 23},
    {"Titulo" : "pirca", "tocou": 32},
    {"Titulo" : "Pipinha", "tocou": 33},
    {"Titulo" : "Tutut", "tocou": 100},
]

print(max(musicas, key=lambda musica: musica['tocou'])["Titulo"]) #Qual Mais Tocou, retornando Somente o Nome
print(min(musicas, key=lambda musica: musica['tocou'])["Titulo"]) #Qual Menos Tocou, retornando Somente o Nome

#Desafio! Como encontrar a música mais tocada sem utilizar Min(), Max() e Lambda
maior= -999
menor = 999
for r in range(0,len(musicas)):
    if musicas[r]['tocou'] > maior:
        maior = musicas[r]['tocou']
        maio = musicas[r]['Titulo']
    if musicas[r]['tocou'] < menor:
        menor = musicas[r]['tocou']
        meno = musicas[r]['Titulo']
       
print(f"maior: {maio}, menor: {meno}")