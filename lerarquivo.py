from numpy import loadtxt


class IniciarGrafo:
    def __init__(self, vertices: list):
        with open('./grafos_de_entrada/0_grafo.txt') as file:
            linha = None

            for _ in range(4):
                file.readline()

            while linha != []:
                linha = file.readline().split()

                if linha != []:
                    self.__addAdjacente(int(linha[0]), int(linha[1]), vertices)
                    

    def __addAdjacente(self, u: int, v: int, vertices):
        if not v in vertices[u - 1].getAdjacentes():
            vertices[u - 1].setAdjacente(v)
