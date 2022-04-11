from numpy import loadtxt


class IniciarGrafo:
    def __init__(self):
        self.numArquivo = 0
        with open(open('./grafos_de_entrada/0_grafo.txt')) as file:
            dados = loadtxt(file, delimiter=' ')

        print(dados)


IniciarGrafo()
