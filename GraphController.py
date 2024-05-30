import networkx as nx
import matplotlib.pyplot as plt
from networkx.utils import pairwise


class Graph:
    def __init__(self, diccionario):    #constructor clase grafo
        self.g = nx.Graph()             #creo el grafo con el metodo de networkx.Graph()
        self.diccionario = diccionario  #diccionario de nombres de alumnos y su lista de relaciones
        self.agregarnodos()             #ejecuto esta funcion para automaticamente rellenar el grafo cuando lo creo

    def agregarnodos(self):              #funcion para agregar los nodos a partir de los datos
        for key in self.diccionario:     #bucle foreach para cada key del diccionario
            self.crearnodo(key)          #creo un nodo por cada key del diccionario (nombre alumno)
            for relacion in self.diccionario[key]:   #por cada relacion de cada llave (for anidado)
                self.relacionar(key, relacion[0], relacion[1])  #establezco la relacion entre la llave y ese otro nodo

    def crearnodo(self, nombre):         #metodo para crear nodos
        self.g.add_node(nombre)

    def relacionar(self, nombreA, nombreB, valor):   #metodo para relacionar nodos
        self.g.add_edge(nombreA, nombreB, weight=valor)

    def mostrargrafo(self):
        forma = nx.spring_layout(self.g)   #creo la forma del grafo (layout)
        datosaristas = nx.get_edge_attributes(self.g, name='weight') #obtengo los datos de las aristas
        nx.draw(self.g, forma, with_labels=True, node_color='#BBBBBB', node_size=1000)  #dibujo los nodos
        nx.draw_networkx_edge_labels(self.g, forma, edge_labels=datosaristas)  #agrego los datos de las aristas
        plt.show()  #muestro el grafico en pantalla

    def hallarcamino(self, alumno1, alumno2):
        camino = nx.dijkstra_path(self.g, alumno1, alumno2, weight='weight')  #obtengo el camino mas cortos segun el peso
        sg = self.g.edge_subgraph(pairwise(camino))  #creo un subgrafo, importante el uso de pairwise
        layout = nx.spring_layout(sg)   #a partir de aca hago lo mismo q en mostrar grafo
        labels2 = nx.get_edge_attributes(sg, name='weight')
        nx.draw(sg, layout, with_labels=True, node_color='#BBBBBB', node_size=1000)
        nx.draw_networkx_edge_labels(sg, layout, edge_labels=labels2)
        plt.show()
