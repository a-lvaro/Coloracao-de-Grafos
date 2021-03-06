from vertice import Vertice
from cores import Cor
from lerarquivo import IniciarGrafo
import numpy as np


class Grafo:
    def __init__(self, numArquivo: int) -> None:
        self.__vertices = []
        self.__numArquivo = str(numArquivo)
        self.__listaPrioridade = []

        for i in range(15):
            self.__vertices.append(Vertice(i + 1))

        self.iniciarGrafo()
        self.__listaPrioridade = self.listaPrioridade()

    def iniciarGrafo(self) -> None:
        IniciarGrafo(self.__vertices, self.__numArquivo)

    def cores(self) -> None:
        Cor(self.__vertices, self.__listaPrioridade)

    def mostrarCores(self) -> None:
        for vertice in self.__vertices:
            print('     {} : {}'.format(vertice.getVertice(), vertice.getCor()))

    '''--------------------------------------------------------
        como a lista começa em 0 e os vértices em 1,
        para achar a localização dos vértices na lista será n - 1
        -------------------------------------------------------'''

    def listaPrioridade(self):
        listaPrioridade = []

        for vertice in self.__vertices:
            listaPrioridade.append(
                [vertice.getVertice(), len(vertice.getAdjacente())])

        listaPrioridade = np.array(listaPrioridade)
        listaPrioridade = listaPrioridade[listaPrioridade[:, 1].argsort()]
        return listaPrioridade[::-1]

    def grafoPlanar(self) -> bool:
        qtdAresta = 0

        for vertice in self.__vertices:
            qtdAresta += len(vertice.getAdjacente())

        return qtdAresta <= 3 * len(self.__vertices) - 6
