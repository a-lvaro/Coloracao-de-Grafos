from time import process_time_ns


class Cor:
    def __init__(self, vertices, pivo):
        self.__vertices = vertices
        adjacentes = [pivo]

        # while adjacentes:
        for i in range(3):
            pivo = adjacentes.pop(0)

            print('\n\npivo: ', pivo)
            self.__vertices[pivo - 1].setCor()
            print('cor: ', self.__vertices[pivo - 1].getCor())
            self.__removeCorAdjacentes(pivo)

            for aux in self.__vertices[pivo - 1].getAdjacentes():
                if type(self.__vertices[aux - 1].getCor()) == list and aux not in adjacentes:
                    adjacentes.append(aux)

            print('lista percorrer: ', adjacentes)

    def __removeCorAdjacentes(self, pivo: int):
        print('ADJACENTES ao vértice', self.__vertices[pivo-1].getAdjacentes())
        for vertice in self.__vertices[pivo - 1].getAdjacentes():
            self.__vertices[vertice -
                            1].removeCor(self.__vertices[pivo - 1].getCor())
