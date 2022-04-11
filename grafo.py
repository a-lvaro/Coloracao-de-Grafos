from vertice import Vertice
from cores import Cor
from lerarquivo import IniciarGrafo


class Grafo:
    def __init__(self):
        self.__vertices = []
        self.numArquivo = 0

        for i in range(15):
            self.__vertices.append(Vertice(i + 1))

        self.iniciarGrafo()

        for vertice in self.__vertices:
            print(vertice.getAdjacentes())

    def iniciarGrafo(self) -> None:
        IniciarGrafo(self.__vertices)

    def cores(self) -> None:
        Cor(self.__vertices, 7)

    def mostrarCores(self):
        for vertice in self.__vertices:
            print('{} : {}'.format(vertice.getVertice(), vertice.getCor()))

    '''--------------------------------------------------------
        como a lista começa em 0 e os vértices em 1,
        para achar a localização dos vértices na lista será n - 1
        -------------------------------------------------------'''
