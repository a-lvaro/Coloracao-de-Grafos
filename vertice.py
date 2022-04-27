class Vertice:
    def __init__(self, vertice: int) -> None:
        self.__vertice = vertice
        self.__adjacentes = []
        self.__cor = ['branco', 'vermelho', 'verde', 'preto']

    def setAdjacente(self, v: int) -> None:
        self.__adjacentes.append(v)

    def getAdjacente(self) -> list:
        return self.__adjacentes

    def setCor(self) -> None:
        if self.__cor != []:
            self.__cor = self.__cor.pop(0)

        elif self.__cor != []:
            self.__cor = self.__cor[0]

    def getCor(self) -> str or list:
        return self.__cor

    def removeCor(self, cor: str) -> None:
        if cor in self.__cor:
            self.__cor.remove(cor)

    def getVertice(self) -> int:
        return self.__vertice
