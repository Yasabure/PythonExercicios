"""
Filter

Filter() -> Serve para filtrar dados em uma coleção
import statistics

dados = [1,2,3,4,5,-1,2.5,3.9, 10, 22]

#Calculando A média dos dados

media = statistics.mean(dados)
# Obs: Filter() Recebe dois parametros, sendo  uma função e um interavel.

res = filter(lambda x: x > media, dados)
# X esta recebendo cada dado de 'dados'
print(list(res))
print(media)
print(list(res))
#Assim Como no map, o filter() após ser conjvertido e mostrado mais de uma vez seu resultado, ele é apagado

paises = ['', 'Argentina', 'Brasil', 'Chile','']
res = filter(None, paises) # none é um tipo de string, sendo a string 'Vazia'
print(list(res))

#Diferença entre Map e Filter

Map aplica uma função em todos os valores
Filter Aplica uma função que vai filtrar e pegar apenas as que são de acordo com a função utilizada

# Exemplo mais Complexo

users = [
    {"username": "Pedro", "tweets": ["Eu Adoro bolos", "Eu adoro Pizzas"]},
    {"username": "samuel", "tweets": ["Eu adoro Pizzas"]},
    {"username": "Leo", "tweets": []},
    {"username": "Macaco", "tweets": ["Eu Adoro bolos"]},
]
#Filtar users inativos

#inativos1 = list(filter(lambda u: len(u['tweets'])== 0, users))
#inativos2 = list(filter(lambda usuario: not usuario['tweets'], users))
# O Not passa vendo se há algo no valor, caso tenha é false, se não é true. Logo se n tem nada ele da true e filtra

print(inativos)
"""

#Combinar Filter() e Map()

nomes = ['Leonardo', 'Ana', 'Caio','Yasmin']

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
#Aqui o Map está tendo a função de receber a função 'Lambda' e o seu interavel só é dado caso o 'Filter' aprove o valor

print(lista)
