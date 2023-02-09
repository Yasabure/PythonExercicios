def km_gasolina(km, gasolina):
    if km/gasolina < 8:
        return 'Venda o Carro'
    elif km/gasolina >= 8 and km/gasolina <= 14:
        return 'Carro Econômico'
    elif km/gasolina > 14:
        return 'Super Economico'

print(km_gasolina(300, 10))