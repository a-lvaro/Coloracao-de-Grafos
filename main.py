from grafo import Grafo


for i in range(15):
    g = Grafo(i)

    if g.grafoPlanar():
        listaPrioridade = g.listaPrioridade()
        print('_________')
        print(listaPrioridade)
        g.cores(listaPrioridade)
        g.mostrarCores()

    else:
        print(i, '  :  Não é um grafo planar')
