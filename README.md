# Coloracao-de-Grafos
Trabalho da disciplina de algoritmo em grafos, o qual tem como objetivo a colorir os grafos com 4 cores.

O algritmo consegue colorir todos os grafos que são planares, caso os grafos não sejam planares, provavelmente o algoritmo não conseguirá resolvê-lo.
Foi usado a heurística de que o vértice com mais aresta é o mais difícil de colorir, dessa forma, foi feita uma lista com os vértice de maior grau para menor. Em seguida, o algoritmo foi dando a coloração para esse grafo.

Caso o algoritmo não conseiga preencher todas os vértices, o programa retornará '[]' para aquele vértice.

grafo planar: quatidade de aresta <= 3 * quantidade de vértices - 6
