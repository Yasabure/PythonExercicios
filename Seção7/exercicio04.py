def quadrado_perfeito(a):
    if a > 0:
        for r in range(0,32):
            if a == r * r:
                return f'{a} é um Quadrado perfeito de {r}'

print(quadrado_perfeito(25))