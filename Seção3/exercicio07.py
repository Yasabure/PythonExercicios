esfera = 0
limpeza = 0
cabo = 0 
quebrado = 0
total = 0

codigo = int(input("Informe o Código do Mause: "))
while codigo != 0:
    print("Identifique o erro")
    print(" 1 = Necessita de esfera")
    print(" 2 = Necessita de limpeza")
    print(" 3 = Necessita de cabo ou conector")
    print(" 4 = Quebrado")
    erro = int(input("Identifique o Erro: "))
    if erro == 1:
        esfera = esfera + 1
    elif erro == 2:
        limpeza = limpeza + 1
    elif erro == 3:
        cabo = cabo + 1
    elif erro == 4:
        cabo = cabo + 1
    else:
        total = total - 1 
        print("Erro não identificado")
    total = total + 1
    codigo = int(input("Informe o Código do Mause: "))


limpeza1 = (limpeza * 100) / total
esfera1 = (esfera * 100) / total
cabo1 = (cabo * 100) / total
quebrado1 = (quebrado * 100) / total

print("Quantidade de Mouses: {0}".format(total))
print("     Situação                    Quantidade   Percentual")
print("1 = Necessita esfera                {0}          {1}".format(esfera, esfera1))
print("2 = Necessita Limpeza               {0}          {1}".format(limpeza, limpeza1))
print("3 = Necessita De cabo ou Conector   {0}          {1}".format(cabo, cabo1))
print("4 = Quebrado                        {0}          {1}".format(quebrado, quebrado1))

    