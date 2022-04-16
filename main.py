from grafo import Grafo


for i in range(1):
    g = Grafo(i)

    if g.grafoPlanar():
        print(
            f'\n\n{i} :  Como não é um grafo planar, não é possível colori-lo com apenas quatro cores \n')
        print('    Lista com a possível coloração')

    else:
        print('\n\nColoração\n')

    # g.cores()
    # g.mostrarCores()
