import networkx as nx
import matplotlib.pyplot as plt
from networkx.utils import pairwise


class Graph:
    def __init__(self, datos):
        self.g = nx.Graph()
        self.datos = datos
        self.agregarnodos()

    def agregarnodos(self):
        for key in self.datos:
            self.crearnodo(key)
            for relacion in self.datos[key]:
                self.crearnodo(relacion[0])
                self.relacionar(key, relacion[0], relacion[1])

    def crearnodo(self, nombre):
        self.g.add_node(nombre)

    def relacionar(self, nombreA, nombreB, valor):
        self.g.add_edge(nombreA, nombreB, weight=valor)

    def mostrargrafo(self):
        layout = nx.spring_layout(self.g)
        labels2 = nx.get_edge_attributes(self.g, name='weight')
        nx.draw(self.g, layout, with_labels=True, node_color='#BBBBBB', node_size=1000)
        nx.draw_networkx_edge_labels(self.g, layout, edge_labels=labels2)
        plt.show()

    def hallarcamino(self, alumno1, alumno2):
        camino = nx.dijkstra_path(self.g, alumno1, alumno2, weight='weight')
        sg = self.g.edge_subgraph(pairwise(camino))
        layout = nx.spring_layout(sg)
        labels2 = nx.get_edge_attributes(sg, name='weight')
        nx.draw(sg, layout, with_labels=True, node_color='#BBBBBB', node_size=1000)
        nx.draw_networkx_edge_labels(sg, layout, edge_labels=labels2)
        plt.show()
