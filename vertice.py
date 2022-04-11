from random import choice


class Vertice:
    def __init__(self, vertice) -> None:
        self.vertice = vertice
        self.__adjacentes = []
        self.__cor = ['branco', 'vermelho', 'verde', 'preto', None]

    def setAdjacente(self, v: int) -> None:
        self.__adjacentes.append(v)

    def getAdjacentes(self) -> list:
        return self.__adjacentes

    def setCor(self) -> None:
        self.__cor.remove(None)
        self.__cor = choice(self.__cor)

    def getCor(self) -> str or list:
        return self.__cor

    def removeCor(self, cor: str) -> None:
        try:
            if cor in self.__cor:
                self.__cor.remove(cor)

        except:
            print("\n\n################")
            print('Vertice: ', self.vertice)
            print('removeCor: ', self.__cor)
            print('remover: ', cor)

    def getAresta(self):
        return self.aresta

    def setVertice(self, vertice):
        self.__vertice = vertice

    def getVertice(self) -> int:
        return self.__vertice
