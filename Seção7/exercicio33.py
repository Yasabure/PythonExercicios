def fatorando(num):
     lista = []
     soma = 0
     resultado = num
     for r in range(1, num):
         resultado=resultado *(num-r) 
     resultado = str(resultado)
     print(resultado)
     for i in resultado:
          lista.append(i)
          soma = soma + int(i)
     print(soma)

fatorando(12)