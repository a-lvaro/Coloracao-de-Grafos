from grafo import Grafo


for i in range(60):
    g = Grafo(i)

    if g.grafoPlanar():
        print('\n\nColoração\n')

    else:
        print(
            f'\n\n{i} :  Como não é um grafo planar, não é possível colori-lo com apenas quatro cores, segundo o teorema da 4-coloração \n')
        print('     Lista com a possível coloração\n')

    g.cores()
    g.mostrarCores()
