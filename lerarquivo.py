class IniciarGrafo:
    def __init__(self, vertices :list):
        file = open('./grafos_de_entrada/' +
                    self.numArquivo.__str__() + '_grafo.txt')
        for _ in range(4):
            linha = file.readline()

        while linha != []:
            linha = file.readline().split()

            if linha != []:
                self.addAdjacente(int(linha[0]), int(linha[1]))

        file.close()
