from cmath import inf
from random import choice


class Vertice:
    def __init__(self, vertice) -> None:
        self.vertice = vertice
        self.adjacentes = []
        self.__cor = ['branco', 'vermelho', 'verde', 'preto', None]

    def addAdjacente(self, v: int) -> None:
        # if u == self.vertice:
        self.adjacentes.append(v)
        self.adjacentes.sort()

    def setCor(self) -> None:
        self.__cor.remove(None)
        self.__cor = choice(self.__cor)

    def getCor(self) -> str or list:
        return self.__cor

    def removeCor(self, cor: str) -> None:
        if cor in self.__cor:
            self.__cor.remove(cor)

    def getAdjacentes(self):
        return self.adjacentes
