def quadruplo_fatorial(n: int)-> int:
    a = n * 2
    b = 1
    c = 1
    for r in range(1, n+1):
        b *= r
    for i in range(1, a+1):
        c *= i
    print(c/b)
    print(b)
    print(c)

quadruplo_fatorial(3)
        

    