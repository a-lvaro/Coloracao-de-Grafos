from grafo import Grafo


g = Grafo(1, 7)

listaPrioridade = g.listaPrioridade()
print(listaPrioridade)
g.cores(listaPrioridade)
g.mostrarCores()
