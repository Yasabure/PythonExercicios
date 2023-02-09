def hiperfatorial(n: int) -> int:
    resultado = 1
    for r in range(1, n+1):
        for i in range(1, r+1):
            resultado *= i
    print(resultado)


hiperfatorial(5)
