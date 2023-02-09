nome = input("Informe o Nome: ")
senha = input("Informe a Senha: ")
while senha == nome:
    print("Senha não pode ser igual ao nome")
    nome = input("Informe o Nome: ")
    senha = input("Informe a Senha: ")
print("Hello Word")