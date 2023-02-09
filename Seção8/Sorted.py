"""
Sorted

Obs: Sorted não é o mesmo que 'sort()'
Sorted Só funciona em listas
Sorted() pode ser utilizado com qualquer interavel
Sorted() Serve para ordenar
Sorted() Sempre retornara uma lista, mesmo que o elementos do interavel sejam, tupla. lista, set...
#Podemos Alterar o retorno de uma lista ao utilizar Sorted() Ex:
Print(sorted(lista)) #Retorna em lista
Print(tuple(sorted(lista))) #retorna em tupla
lista = [1,3,57,1235,-2,-1,0,5451,-2315,213]
print(sorted(lista)) #Do menor para o maior, Não modifica a propria lista, gera uma nova 
print(sorted(lista, reverse=True)) #Ordena do maior para o menor

#Utilizando o sorted() De forma mais complexa

users = [
    {"username": "Pedro", "tweets": ["Eu Adoro bolos", "Eu adoro Pizzas"]},
    {"username": "samuel", "tweets": ["Eu adoro Pizzas"]},
    {"username": "Leo", "tweets": []},
    {"username": "Macaco", "tweets": ["Eu Adoro bolos"]},
]
print(users)
print(sorted(users, key=len))#Aqui sairá da mesma forma que o print(users), ele conta as chaves e não os caracteres
#Ordenado Pelo Ursername Ordem alfabética
print(sorted(users, key=lambda users: users['username'])) 
#Ordenado Pelo Número De Tweets
print(sorted(users, key=lambda users: len(users["tweets"])))

"""
musicas = [
    {"Titulo" : "Bixa assumida", "tocou": 3},
    {"Titulo" : "Tarada", "tocou": 23},
    {"Titulo" : "piroca", "tocou": 32},
    {"Titulo" : "Pipinha", "tocou": 33},
    {"Titulo" : "Tutut", "tocou": 100},
]
print(sorted(musicas, key=lambda musica: musica['tocou']))

print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))





