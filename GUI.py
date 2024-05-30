import tkinter as tk
from tkinter import messagebox
from GraphController import Graph
from DataLoader import DataLoader


class UserInterface:
    def __init__(self):
        self.g = None
        root = tk.Tk()
        root.title("POO 2 - Trabajo Practico Grafos")
        root.geometry("600x300")
        # frame izquierdo para botones
        izquierda = tk.Frame(root)
        izquierda.pack(side="left", padx=10, pady=10, anchor='n')
        botones = tk.Frame(izquierda, bg='white', padx=30, pady=30)
        botones.pack()
        boton1 = tk.Button(botones, text="Elegir primer Excel", command=lambda: self.cargarexcel('test.xlsx'))
        boton1.pack(pady=5)
        boton2 = tk.Button(botones, text="Elegir segundo Excel", command=lambda: self.cargarexcel('test2.xlsx'))
        boton2.pack(pady=5)
        # frame derecho para el dijkstra
        derecha = tk.Frame(root)
        derecha.pack(side="right", padx=10, pady=10, anchor='n')
        textodijkstra = tk.Label(derecha, text="Escribe dos alumnos para encontrar su camino mas corto:")
        textodijkstra.pack(pady=5)
        alu1 = tk.Entry(derecha)
        alu1.pack(pady=5)
        alu2 = tk.Entry(derecha)
        alu2.pack(pady=5)
        botondijkstra = tk.Button(derecha, text="Hallar camino minimo", command=lambda: self.hallarminimo(alu1.get(), alu2.get()))
        botondijkstra.pack(pady=5)
        root.mainloop()

    def cargarexcel(self, archivo):
        dl = DataLoader(archivo, 'Hoja 1')
        dl.loaddata()
        self.g = Graph(dl.nodos)
        self.g.mostrargrafo()

    def hallarminimo(self, alu1, alu2):
        if self.g is None:
            tk.messagebox.showinfo("No se pudo calcular", "No se eligio Excel")
        else:
            self.g.hallarcamino(alu1, alu2)
