from vertice import Vertice
from cores import Cor
from lerarquivo import IniciarGrafo
import numpy as np


class Grafo:
    def __init__(self, numArquivo: int, verticeInicio: int):
        self.__vertices = []
        self.__numArquivo = str(numArquivo)
        self.__verticeInicio = verticeInicio

        for i in range(15):
            self.__vertices.append(Vertice(i + 1))

        self.iniciarGrafo()

        for i, vertice in enumerate(self.__vertices):
            print(i, '  :  ', vertice.getAdjacentes())

    def iniciarGrafo(self) -> None:
        IniciarGrafo(self.__vertices, self.__numArquivo)

    def cores(self, listaPrioridade) -> None:
        Cor(self.__vertices, self.__verticeInicio, listaPrioridade)

    def mostrarCores(self):
        for vertice in self.__vertices:
            print('{} : {}'.format(vertice.getVertice(), vertice.getCor()))

    '''--------------------------------------------------------
        como a lista começa em 0 e os vértices em 1,
        para achar a localização dos vértices na lista será n - 1
        -------------------------------------------------------'''

    def listaPrioridade(self):
        listaPrioridade = []

        for i, vertice in enumerate(self.__vertices):
            listaPrioridade.append([i, len(vertice.getAdjacentes())])

        listaPrioridade = np.array(listaPrioridade)
        listaPrioridade = listaPrioridade[listaPrioridade[:, 1].argsort()]
        return listaPrioridade[::-1]
