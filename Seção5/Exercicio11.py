vetor = []
pos = []
neg = 0
i = -3
for r in range(7):
    vetor.append(i)
    if i < 0:
        neg = neg + 1
    else:
        pos.append(i) 
    i = i + 1  
print("Esse vetor Possui {0} números negativos e a soma dos números positivos é {1}".format(neg, sum(pos)))
