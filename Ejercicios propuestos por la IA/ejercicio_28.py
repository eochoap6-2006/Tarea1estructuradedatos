# Ejercicio 28 - Organizador de grupos de proyecto
class GruposProyecto:
    def __init__(self):
        self.grupos = {}
    def crear_grupo(self, nombre):
        if nombre not in self.grupos:
            self.grupos[nombre] = []
    def agregar_integrante(self, grupo, estudiante):
        if grupo in self.grupos:
            self.grupos[grupo].append(estudiante)
    def grupo_menor_integrantes(self):
        if len(self.grupos) == 0:
            return None
        grupo_menor = None
        menor_cantidad = None
        for grupo, integrantes in self.grupos.items():
            cantidad = len(integrantes)
            if menor_cantidad is None or cantidad < menor_cantidad:
                menor_cantidad = cantidad
                grupo_menor = grupo
        return grupo_menor
gp = GruposProyecto()
gp.crear_grupo("Grupo A")
gp.crear_grupo("Grupo B")
gp.agregar_integrante("Grupo A", "Ana")
gp.agregar_integrante("Grupo A", "Luis")
gp.agregar_integrante("Grupo B", "Pedro")
print(gp.grupos)
print(gp.grupo_menor_integrantes())
