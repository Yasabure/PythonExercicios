def soma_diagonalprincipalabaixo(matriz: list) ->  list:
      m = 1
      soma = 0
      for l in range(0,3):
         for c in range(0, m):
             if l == c:
                 m += 1
             if m == 0:
                 c = 2
             if l != c and l > 0:
                soma = soma + matriz[l][c]      
      print(soma)

soma_diagonalprincipalabaixo([[1,2,3],[4,5,6],[7,8,9]])


