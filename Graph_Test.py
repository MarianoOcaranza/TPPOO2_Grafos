from Alumno import Alumno
from DataLoader import DataLoader
from GraphController import Graph


dl = DataLoader('test.xlsx', 'Hoja 1')
dl.loaddata()

grafo1 = Graph(dl.nodos)
grafo1.mostrargrafo()
grafo1.hallarcamino('Lautaro', 'Lucas')
