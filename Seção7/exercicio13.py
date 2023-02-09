def calculadora_junior(a, funcao, b):
    if funcao == '+':
        return a + b
    elif funcao == '-':
        return a - b
    elif funcao == '*':
        return a * b
    elif funcao == '/':
        return a / b
    return 'Função Invalida'

print(calculadora_junior(1, 'b', 6))
    
