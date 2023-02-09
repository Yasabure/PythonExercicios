def detector_anagramana(a: str, b: str) -> str:
    # .lower = Converter todas as letras da string para minusculo
    a = a.lower()
    b = b.lower()
    anagrama = 0
    if len(a) == len(b):
        a = list(a)
        for r in (a):
            if b.count(r) >= 1:
                anagrama += 1
    if anagrama == len(a):
        print(f'Verdadeiro')
    else:
        print(f'Falso')

detector_anagramana('Alergia', 'alegria')