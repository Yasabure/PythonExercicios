def medida_triangulo(medida1, medida2, medida3):
      if medida1 <= 0 or medida2 <= 0 or medida3 <= 0:
            return 'Valores invalidos'
      if medida1 + medida2 <= medida3 or medida3 + medida2 <= medida1 or medida3 + medida1 <= medida2:
            return 'Não é um Triangulo'
      if medida1 == medida2 and medida2 == medida3:
            return 'O Triângulo equilátero'
      if medida1 == medida2 or medida2 == medida3 or medida3 == medida1:
            return 'O Triângulo isosceles'
      if medida1 != medida2 and medida2 != medida3 and medida1 != medida3:
            return 'O Triangulo Escaleno'
      
      

print(medida_triangulo(2, 3, 3))
