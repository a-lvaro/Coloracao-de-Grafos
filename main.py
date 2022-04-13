from grafo import Grafo


g = Grafo(3)

listaPrioridade = g.listaPrioridade()
print(listaPrioridade)
g.cores(listaPrioridade)
g.mostrarCores()
