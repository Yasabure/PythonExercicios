def analise_pessoas(v1: list):
    media = 0
    idade = 0
    maior = 0
    privilegiada = 0

    for r in range (0, len(v1)):
        if v1[r][1] == 'castanho' and v1[r][2] == 'preto':
            idade += v1[r][3]
            media +=1
        if v1[r][3] > maior:
            maior = v1[r][3]
        if v1[r][0] == 'f' and v1[r][1] == 'azul' and v1[r][2] == 'loiro' and v1[r][3] >= 18 and v1[r][3] <= 35:
            privilegiada +=1
        
    media = idade/media
    print(f'Media de idade De P/com Olhos Castanhos e Cabelos Pretos: {media}, Maior idade: {maior}, Privilegiadas: {privilegiada}')

    
analise_pessoas([['f', 'azul','loiro', 18],['f', 'azul','preto', 18],['m', 'azul','preto', 39],['m', 'azul','preto', 18],['m', 'castanho','preto', 18]])