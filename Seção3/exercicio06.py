n = int (input("Informe um Número: "))
while n < 1 or n > 10:
    n = int (input("Informe um Número: "))
print("Tabuada do {0}".format(n))
for i in range(1, 11):
        print("{0} X {1} = {2} ".format(n, i, (n * i)))