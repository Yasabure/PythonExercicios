def fatorial_exponencial(n: int) -> int:
    total = 0
    n_elevado = n
    a = n - 1
    for r in range(1, n):
        if n - a >= 1:
            elevado = n - a
            for l in range(1, elevado-1):
                if total == 0:
                    total = elevado
                total *= elevado
            if n - 1 == 2:
                total = 2
        a -= 1
    for i in range(1, total):
        n_elevado *= n

    print(f"O Resultado de {n} Elevado a {total} = {n_elevado}")


fatorial_exponencial(6)
