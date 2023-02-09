def fatorial_duplo(n: int) -> int:
    fatorial = 1
    while n % 2 ==0:
        n = int(input(f'Informe um número IMPAR'))
    for r in range(1, n + 1):
        if r % 2 != 0:
            fatorial *= r

    print(fatorial)

fatorial_duplo(7)