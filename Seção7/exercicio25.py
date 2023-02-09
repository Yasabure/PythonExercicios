def retorno(n):
    a = 1
    total = 0
    for r in range(0, n):
        b = a + 3
        c = (a ** 2 + 1) / b
        total += c
        a += 1
    print(total)


retorno(8)
