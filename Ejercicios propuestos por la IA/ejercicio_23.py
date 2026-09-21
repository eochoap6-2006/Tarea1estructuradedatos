# Ejercicio 23 - Biblioteca de libros
class Biblioteca:
    def __init__(self):
        self.libros = {}
    def agregar_libro(self, titulo, paginas):
        self.libros[titulo] = paginas

    def total_paginas(self):
        return sum(self.libros.values())
    def libros_por_paginas(self, minimo, maximo):
        encontrados = []
        for titulo, paginas in self.libros.items():
            if paginas >= minimo and paginas <= maximo:
                encontrados.append(titulo)
        return encontrados
b = Biblioteca()
b.agregar_libro("Python Básico", 180)
b.agregar_libro("Algoritmos", 250)
b.agregar_libro("Bases de Datos", 320)
print(b.total_paginas())
print(b.libros_por_paginas(150, 260))
