from operator import concat


def concatena_(str1: str,str2: str, n: int):
    if n > len(str2):
        n = int(input(f"Informe Um Número menor ou igual a {len(str2)}:"))
    str3 = str2[0:n]
    return concat(str1, str3)

print(concatena_('Amo ','Te Comer', 5))