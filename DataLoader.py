import pandas as pd

from Alumno import Alumno


class DataLoader:
    def __init__(self, archivo, nombrehoja):
        self.df = pd.read_excel(archivo, sheet_name=nombrehoja, header=None)  # creo el dataframe con el excel
        self.nodos = {}

    def loaddata(self):
        for rowindex, dataseries in self.df.iterrows():
            if dataseries[0] in self.nodos.keys():
                self.nodos.get(dataseries[0]).append((dataseries[1], dataseries[2]))
            else:
                nuevonodo = Alumno(dataseries[0])
                nuevonodo.agregarrelacion((dataseries[1], dataseries[2]))
                self.nodos[nuevonodo.nombre] = nuevonodo.relaciones
