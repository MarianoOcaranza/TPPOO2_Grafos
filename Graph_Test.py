from GraphController import Graph

grafo1 = Graph()

grafo1.crearnodo("Jose")
grafo1.crearnodo("Pedro")
grafo1.crearnodo("Agustin")
grafo1.crearnodo("Josefina")

grafo1.relacionar("Jose", "Pedro", 3)
grafo1.relacionar("Jose", "Agustin", 1)
grafo1.relacionar("Agustin", "Pedro", 1)
grafo1.relacionar("Agustin", "Josefina", 3)
grafo1.mostrargrafo()
grafo1.hallarcamino("Jose", "Pedro")
