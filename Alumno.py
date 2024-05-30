class Alumno:
    def __init__(self, nombre):  #'constructor de la clase alumno.
        self.nombre = nombre     #'nombre del alumno
        self.relaciones = []     #' lista de adyacencias (va a contener una tupla (alumnorelacionado, peso)

    def agregarrelacion(self, relacion):  #funcion para agregar una relacion a la lista
        self.relaciones.append(relacion)  #el metodo list.append() agrega un elemento
