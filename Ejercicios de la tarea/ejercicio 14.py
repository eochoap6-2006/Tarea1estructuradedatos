#Ejercicio 14 - Mapeo de estudiantes a notas
class RegistroNotas:
    def __init__(self):
        self.notas = {}
    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota
    def estudiantes_aprobados(self, nota_minima):
        aprobados = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)
        return aprobados
    def mejor_estudiante(self):
        if len(self.notas) == 0:
            return None
        mejor_nombre = None
        mejor_nota = -1
        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante
        return (mejor_nombre, mejor_nota)
rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
rn.registrar("Carlos", 88)
print(rn.estudiantes_aprobados(70))
print(rn.mejor_estudiante())