class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.relaciones = []

    def agregarrelacion(self, relacion):
        self.relaciones.append(relacion)
