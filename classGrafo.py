from tkinter import E

from numpy import true_divide
from classVertice import Vertice
from cores import Cor


class Grafo:
    def __init__(self):
        self.vertices = []
        self.qtdVertices = 15
        self.numArquivo = 0

        for i in range(15):
            self.vertices.append(Vertice(i + 1))

        self.iniciarGrafo()

        for vertice in self.vertices:
            print(vertice.getAdjacentes())

    def iniciarGrafo(self) -> None:
        file = open('./grafos_de_entrada/' +
                    self.numArquivo.__str__() + '_grafo.txt')
        for _ in range(4):
            linha = file.readline()

        while linha != []:
            linha = file.readline().split()

            if linha != []:
                self.addAdjacente(int(linha[0]), int(linha[1]))

    def addAdjacente(self, u: int, v: int):
        if not v in self.vertices[u - 1].adjacentes:
            self.vertices[u - 1].addAdjacente(v)
            #self.vertices[v - 1].addAdjacente(u, v)

    def cores(self) -> None:
        Cor(self.vertices, 7)

    def mostrarCores(self):
        for vertice in self.vertices:
            print('{} : {}'.format(vertice.vertice, vertice.getCor()))

    '''--------------------------------------------------------
        como a lista começa em 0 e os vértices em 1,
        para achar a localização dos vértices na lista será n - 1
        -------------------------------------------------------'''

    def getAdjacentes(self, vertice: int) -> list:
        return self.vertices[vertice - 1].aresta
