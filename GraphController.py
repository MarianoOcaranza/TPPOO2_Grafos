import networkx as nx
import matplotlib.pyplot as plt
from Alumno import Alumno
from networkx.utils import pairwise


class Graph:
    def __init__(self, datos):
        self.g = nx.Graph()
        self.datos = datos

    def agregarnodos(self):
        lista = list(self.datos.keys())
        for key in lista:
            self.crearnodo(key.nombre)
            for relacion in self.datos[key]:
                self.crearnodo(relacion[0].nombre)
                self.relacionar(key.nombre, relacion[0].nombre, relacion[1])

    def crearnodo(self, nombre):
        self.g.add_node(nombre)

    def relacionar(self, nombreA, nombreB, valor):
        self.g.add_edge(nombreA, nombreB, weight=valor)

    def mostrargrafo(self):
        layout = nx.circular_layout(self.g)
        labels2 = nx.get_edge_attributes(self.g, name='weight')
        nx.draw(self.g, layout, with_labels=True, node_color='#BBBBBB', node_size=1000)
        nx.draw_networkx_edge_labels(self.g, layout, edge_labels=labels2)
        plt.show()

    def hallarcamino(self, nombre1, nombre2):
        camino = nx.dijkstra_path(self.g, nombre1, nombre2, weight='weight')
        sg = self.g.edge_subgraph(pairwise(camino))
        layout = nx.circular_layout(sg)
        labels2 = nx.get_edge_attributes(sg, name='weight')
        nx.draw(sg, layout, with_labels=True, node_color='#BBBBBB', node_size=1000)
        nx.draw_networkx_edge_labels(sg, layout, edge_labels=labels2)
        plt.show()
