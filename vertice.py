class Vertice:
    def __init__(self, vertice) -> None:
        self.__vertice = vertice
        self.__adjacentesOrientado = []
        self.__adjacentesNaoOrientado = []
        self.__cor = ['branco', 'vermelho', 'verde', 'preto']

    def setAdjacenteOrientado(self, v: int) -> None:
        self.__adjacentesOrientado.append(v)

    def getAdjacentesOrientado(self) -> list:
        return self.__adjacentesOrientado

    def setAdjacentesNaoOrientado(self, v: int) -> None:
        self.__adjacentesNaoOrientado.append(v)

    def getdjacentesNaoOrientado(self) -> list:
        return self.__adjacentesNaoOrientado

    def setCor(self) -> None:
        # self.__cor.remove(None)
        if self.__cor != [] and None not in self.__cor:
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
