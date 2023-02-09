def triangulo(n):
    i = 1
    for r in range(1, n + 1):
        x = (2* i - 1) * '*'
        y = (n - i) * ' '
        print(f"{y} {x}")
        i +=1

        

triangulo(8)
