from classVertice import Vertice
from cores import Cor


class Grafo:
    def __init__(self, vertices: int):
        self.vertices = []
        self.qtdVertices = vertices

        for i in range(vertices):
            self.vertices.append(Vertice(i + 1))

    def addAresta(self, u: int, v: int):
        # grafo não orientado, os dois vértices precisam saber que estão ligados
        if not v in self.vertices[u - 1].aresta:
            self.vertices[u - 1].addAresta(u, v)
            self.vertices[v - 1].addAresta(u, v)

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
