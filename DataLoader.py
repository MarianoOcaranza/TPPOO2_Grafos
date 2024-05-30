import pandas as pd
from Alumno import Alumno

#el diccionario nodos tiene la forma {'nombre': listarelaciones[('nombre', peso)]}


class DataLoader:
    def __init__(self, archivo, nombrehoja):  #constructor del data loader
        self.df = pd.read_excel(archivo, sheet_name=nombrehoja, header=None)  # creo el dataframe con el excel
        self.nodos = {}  #abro el diccionario donde guardo los datos

    def loaddata(self):
        for rowindex, dataseries in self.df.iterrows():  #recorro cada linea del dataframe (leer sobre iterables)
            if dataseries[0] in self.nodos.keys() and dataseries[1] in self.nodos.keys():
                self.nodos.get(dataseries[0]).append((dataseries[1], dataseries[2]))
                self.nodos.get(dataseries[1]).append((dataseries[0], dataseries[2]))
            elif dataseries[0] in self.nodos.keys() and dataseries[1] not in self.nodos.keys():
                nuevonodo = Alumno(dataseries[1])
                nuevonodo.agregarrelacion((dataseries[0], dataseries[2]))
                self.nodos[nuevonodo.nombre] = nuevonodo.relaciones
                self.nodos.get(dataseries[0]).append((dataseries[1], dataseries[2]))
            elif dataseries[0] not in self.nodos.keys() and dataseries[1] in self.nodos.keys():
                nuevonodo = Alumno(dataseries[0])
                nuevonodo.agregarrelacion((dataseries[1], dataseries[2]))
                self.nodos[nuevonodo.nombre] = nuevonodo.relaciones
                self.nodos.get(dataseries[1]).append((dataseries[0], dataseries[2]))
            else:
                nuevonodo1 = Alumno(dataseries[0])
                nuevonodo2 = Alumno(dataseries[1])
                nuevonodo1.agregarrelacion((dataseries[1], dataseries[2]))
                nuevonodo2.agregarrelacion((dataseries[0], dataseries[2]))
                self.nodos[nuevonodo1.nombre] = nuevonodo1.relaciones
                self.nodos[nuevonodo2.nombre] = nuevonodo2.relaciones
