# Ejercicio 30 - Lista de películas
class Peliculas:
    def __init__(self):
        self.peliculas = []
    def agregar_pelicula(self, nombre, genero):
        self.peliculas.append((nombre, genero))
    def peliculas_genero(self, genero):
        encontradas = []
        for pelicula in self.peliculas:
            if pelicula[1] == genero:
                encontradas.append(pelicula)
        return encontradas
    def eliminar_pelicula(self, nombre):
        for pelicula in self.peliculas:
            if pelicula[0] == nombre:
                self.peliculas.remove(pelicula)
                return True
        return False
p = Peliculas()
p.agregar_pelicula("Matrix", "ciencia ficción")
p.agregar_pelicula("Titanic", "romance")
p.agregar_pelicula("Interstellar", "ciencia ficción")
print(p.peliculas_genero("ciencia ficción"))
print(p.eliminar_pelicula("Titanic"))
print(p.peliculas)
