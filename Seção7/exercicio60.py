import string 

def substring(a: str) -> str:
    if a.count(' ') > 0:
        b = list(a)
        for r in range(a.index(' ') +1, len(b)+ 1):
            b.pop(a.index(' '))
        b = ''.join(b)
        print(b)
    else:
        print('-1')
substring('Yasmin')
