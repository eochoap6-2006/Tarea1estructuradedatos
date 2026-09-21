#Ejercicio 8 - Asignador de equipos
class Equipos:
    def __init__(self):
        self.equipos={}

    def crear_equipo(self, nombre_equipo):
        if nombre_equipo not in self.equipos:
            self.equipos[nombre_equipo]=[]

    def agregar_jugador (self, equipo, jugador):
        if equipo in self.equipos:
            self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        if len(self.equipos)==0:
            return None
        equipo_mayor=None
        mayor_cantidad=-1
        for equipo,jugadores in self.equipos.items():
            if len(jugadores)>mayor_cantidad:
                mayor_cantidad=len(jugadores)
                equipo_mayor=equipo
        return equipo_mayor 
# Programa principal

eq = Equipos()

eq.crear_equipo("A")
eq.crear_equipo("B")

eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")

eq.agregar_jugador("B", "Carlos")

print(eq.equipos)
print(eq.equipo_mayor_integrantes())