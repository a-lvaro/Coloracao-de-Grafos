class Cor:
    def __init__(self, vertices, pivo, listaPrioridade):
        self.__vertices = vertices
        adjacentes = [pivo]

        pivo = listaPrioridade[0][0]
        print(pivo)

        self.__conferirCorAdjacente(pivo)
        self.__vertices[pivo - 1].setCor()
        self.__removeCorAdjacentes(pivo)

        # while adjacentes:
        #     pivo = adjacentes.pop(0)

        #     # self.__conferirCorAdjacente(pivo)

        #     self.__vertices[pivo - 1].setCor()

        #     self.__removeCorAdjacentes(pivo)

        #     for aux in self.__vertices[pivo - 1].getAdjacentes():
        #         if type(self.__vertices[aux - 1].getCor()) == list and aux not in adjacentes:
        #             adjacentes.append(aux)

    def __removeCorAdjacentes(self, pivo: int):
        for vertice in self.__vertices[pivo - 1].getAdjacentes():
            # o adjacente a esse vértice já pode ter uma cor
            if type(self.__vertices[vertice - 1].getCor()) == list:
                self.__vertices[vertice -
                                1].removeCor(self.__vertices[pivo - 1].getCor())

    def __conferirCorAdjacente(self, pivo: int):
        for vertice in self.__vertices[pivo - 1].getAdjacentes():
            if type(self.__vertices[vertice - 1].getCor()) != list:
                if self.__vertices[vertice - 1].getCor() in self.__vertices[pivo - 1].getCor():

                    print(vertice, '   Cor adjacente: ',
                          self.__vertices[vertice - 1].getCor())
                    print(pivo, '   Cor pivo:     ',
                          self.__vertices[pivo - 1].getCor())

                    input()
                    cor = self.__vertices[vertice - 1].getCor()
                    self.__vertices[pivo - 1].removeCor(cor)
