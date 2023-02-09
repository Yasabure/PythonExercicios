def notas_alunos(nota1,nota2,nota3,funcao):
    if funcao == 'A' or funcao == 'a':
        return (nota1 + nota2 + nota3)/3
    return (nota1*5)+(nota2*3)+(nota3*2)/10

print(notas_alunos(10,9,8, 'a'))


