class IniciarGrafo:
    def __init__(self, vertices: list, numArquivo: str):
        with open('./grafos_de_entrada/' + numArquivo + '_grafo.txt') as file:
            linha = None

            for _ in range(4):
                file.readline()

            while linha != []:
                linha = file.readline().split()

                if linha != []:
                    self.__addAdjacenteOrientado(
                        int(linha[0]), int(linha[1]), vertices)
                    self.__addAdjacenteNaoOrientado(
                        int(linha[0]), int(linha[1]), vertices)

    def __addAdjacenteOrientado(self, u: int, v: int, vertices):
        if not v in vertices[u - 1].getAdjacentesOrientado():
            vertices[u - 1].setAdjacenteOrientado(v)

    def __addAdjacenteNaoOrientado(self, u: int, v: int, vertices):
        if v not in vertices[u - 1].getdjacentesNaoOrientado():
            vertices[u - 1].setAdjacentesNaoOrientado(v)
            vertices[v - 1].setAdjacentesNaoOrientado(u)
