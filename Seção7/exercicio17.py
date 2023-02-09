def somanumero_entre(numero: int = 0, numero2: int = 0):
    if type(numero) != int or type(numero2) != int:
        return TypeError
    if numero <= 0 or numero2 <= 0:
        return 'Valores Invalidos'
    soma = 0
    for r in range(numero + 1, numero2):
        soma += r
    return soma


print(somanumero_entre(3, 6))
