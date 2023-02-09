from operator import concat


def contatenar_strings(str1: str, str2: str) -> str:
    str3 = concat(str1, str2)
    return str3


print(contatenar_strings('Amo', ' Você'))
