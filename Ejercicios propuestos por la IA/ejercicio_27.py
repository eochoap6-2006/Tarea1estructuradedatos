# Ejercicio 27 - Registro de mascotas
class RegistroMascotas:
    def __init__(self):
        self.mascotas = {}
    def agregar_mascota(self, nombre, edad):
        self.mascotas[nombre] = edad
    def mascotas_mayores(self, edad_minima):
        mayores = []
        for nombre, edad in self.mascotas.items():
            if edad >= edad_minima:
                mayores.append(nombre)
        return mayores
    def edad_promedio(self):
        if len(self.mascotas) == 0:
            return 0
        return sum(self.mascotas.values()) / len(self.mascotas)
rm = RegistroMascotas()
rm.agregar_mascota("Luna", 5)
rm.agregar_mascota("Max", 2)
rm.agregar_mascota("Rocky", 8)
print(rm.mascotas_mayores(4))
print(rm.edad_promedio())
