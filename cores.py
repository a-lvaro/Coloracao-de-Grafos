class Cor:
    def __init__(self, vertices, pivo):
        self.__vertices = vertices
        adjacentes = [pivo]

        while adjacentes:
            pivo = adjacentes.pop(0)

            self.__vertices[pivo - 1].setCor()
            self.__removeCorAdjacentes(pivo)

            for aux in self.__vertices[pivo - 1].getAdjacentes():
                if type(self.__vertices[aux - 1].getCor()) == list and aux not in adjacentes:
                    adjacentes.append(aux)

    def __removeCorAdjacentes(self, pivo: int):
        for vertice in self.__vertices[pivo - 1].getAdjacentes():
            self.__vertices[vertice -
                            1].removeCor(self.__vertices[pivo - 1].getCor())
