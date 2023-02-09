def conversao_sec(h:int = 0, m:int = 0, s:int = 0) -> int:
    if type(h) != int or type(m) != int or type(s) != int:
        return TypeError
    return (h * 3600) + (m * 60) + s

print(conversao_sec(20 ,43 ,30))



