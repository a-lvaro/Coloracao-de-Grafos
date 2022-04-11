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

<<<<<<< HEAD
    def getAresta(self):
        return self.aresta

    def setVertice(self, vertice):
        self.__vertice = vertice

    def getVertice(self) -> int:
        return self.__vertice
=======
    def getAdjacentes(self):
        return self.adjacentes
>>>>>>> 65ec36fe11410aebcd2db697e565e6d4d5102083
