from cmath import inf
from random import choice


class Vertice:
    def __init__(self, vertice) -> None:
        self.vertice = vertice
        self.aresta = []
        self.__cor = ['branco', 'vermelho', 'verde', 'preto', None]

    def addAresta(self, u: int, v: int):
        if u == self.vertice:
            self.aresta.append(v)

        else:
            self.aresta.append(u)

    def setCor(self) -> None:
        self.__cor.remove(None)
        self.__cor = choice(self.__cor)

    def getCor(self) -> str or list:
        return self.__cor

    def removeCor(self, cor: str) -> None:
        if cor in self.__cor:
            self.__cor.remove(cor)

    def getAresta(self):
        return self.aresta

    def setAresta(self, aresta) -> None:
        self.aresta.append(aresta)

    def getAresta(self) -> list:
        return self.aresta
