from Alumno import Alumno
from GraphController import Graph

alu1 = Alumno("Mariano")
alu4 = Alumno("Mariano")
alu2 = Alumno("Emmanuel")
alu3 = Alumno("Pedro")
alu1.agregarrelacion([alu4, 3])


datos = {alu1: alu1.relaciones, alu2: alu2.relaciones}

grafo1 = Graph(datos)
grafo1.agregarnodos()
grafo1.mostrargrafo()
