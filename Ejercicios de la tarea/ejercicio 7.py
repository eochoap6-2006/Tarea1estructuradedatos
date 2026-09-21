#Ejercicio 7 - Mapeador de edades
class GestorPersonas:
    def __init__(self):
        self.personas={}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre]=edad

    def personas_mayores(self, edad_minima):
        mayores=[]
        for nombre,edad in self.personas.items():
            if edad>=edad_minima:
                mayores.append(nombre)
        return mayores

    def edad_promedio(self):
        if len (self.personas)==0:
            return 0
        return sum (self.personas.values())/len(self.personas)
# Programa principal

gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
gp.agregar_persona("Carlos", 40)

print(gp.personas_mayores(18))
print(gp.edad_promedio())