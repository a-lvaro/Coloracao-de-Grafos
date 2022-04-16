from vertice import Vertice
from cores import Cor
from lerarquivo import IniciarGrafo


class Grafo:
    def __init__(self, numArquivo: int, verticeInicio: int) -> None:
        self.__vertices = []
        self.__numArquivo = str(numArquivo)
        self.__verticeInicio = verticeInicio

        for i in range(15):
            self.__vertices.append(Vertice(i + 1))

        self.iniciarGrafo()

        for vertice in self.__vertices:
            print(vertice.getAdjacentes())

    def iniciarGrafo(self) -> None:
        IniciarGrafo(self.__vertices, self.__numArquivo)

    def cores(self) -> None:
        Cor(self.__vertices, self.__verticeInicio)

    def mostrarCores(self) -> None:
        for vertice in self.__vertices:
            print('{} : {}'.format(vertice.getVertice(), vertice.getCor()))

    '''--------------------------------------------------------
        como a lista começa em 0 e os vértices em 1,
        para achar a localização dos vértices na lista será n - 1
        -------------------------------------------------------'''
