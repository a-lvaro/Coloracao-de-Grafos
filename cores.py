class Cor:
    def __init__(self, vertices: list, listaPrioridade: list) -> None:
        for i in listaPrioridade:
            pivo = i[0]
            self.__conferirCorAdjacente(vertices, pivo)
            vertices[pivo - 1].setCor()
            self.__removeCorAdjacentes(vertices, pivo)

    def __conferirCorAdjacente(self, vertices: list, pivo: int) -> None:
        for vertice in vertices[pivo - 1].getAdjacente():
            if type(vertices[vertice - 1].getCor()) != list:
                if vertices[vertice - 1].getCor() in vertices[pivo - 1].getCor():
                    vertices[pivo -
                             1].removeCor(vertices[vertice - 1].getCor())

    def __removeCorAdjacentes(self, vertices: list, pivo: int) -> None:
        for vertice in vertices[pivo - 1].getAdjacente():
            # o adjacente a esse vértice já pode ter uma cor
            if type(vertices[vertice - 1].getCor()) == list:
                vertices[vertice -
                         1].removeCor(vertices[pivo - 1].getCor())
