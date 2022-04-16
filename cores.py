class Cor:
    def __init__(self, vertices, listaPrioridade):
        self.__vertices = vertices

        for i in listaPrioridade:
            pivo = i[0]
            self.__conferirCorAdjacente(pivo)
            self.__vertices[pivo - 1].setCor()
            self.__removeCorAdjacentes(pivo)

    def __removeCorAdjacentes(self, pivo: int) -> None:
        for vertice in self.__vertices[pivo - 1].getAdjacente():
            # o adjacente a esse vértice já pode ter uma cor
            if type(self.__vertices[vertice - 1].getCor()) == list:
                self.__vertices[vertice -
                                1].removeCor(self.__vertices[pivo - 1].getCor())

    def __conferirCorAdjacente(self, pivo: int) -> None:
        for vertice in self.__vertices[pivo - 1].getAdjacente():
            if type(self.__vertices[vertice - 1].getCor()) != list:
                if self.__vertices[vertice - 1].getCor() in self.__vertices[pivo - 1].getCor():
                    cor = self.__vertices[vertice - 1].getCor()
                    self.__vertices[pivo - 1].removeCor(cor)
