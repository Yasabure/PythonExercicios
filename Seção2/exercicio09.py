poluicao = float(input("Informe O Indice de Poluição: "))
if poluicao >= 0.3 and poluicao < 0.4 :
    print("Grupo 1 Suspender as Atividades")
if poluicao >= 0.4 and poluicao < 0.5 :
    print("Grupo 1 e 2 Suspender as Atividades")
if poluicao > 0.5 :
    print("Todos os Grupos Suspender suas Atividades")
if poluicao < 0.3 :
    print("Niveis Acéitaveis")