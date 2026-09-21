# Ejercicio 21 - Registro de asistencia
class ControlAsistencia:
    def __init__(self):
        self.porcentajes = []

    def validar_porcentaje(self, porcentaje):
        if porcentaje >= 0 and porcentaje <= 100:
            return True
        else:
            return False
    def registrar_porcentajes(self, *args):
        for porcentaje in args:
            if self.validar_porcentaje(porcentaje):
                self.porcentajes.append(porcentaje)
        return self.porcentajes
    def promedio_asistencia(self):
        if len(self.porcentajes) == 0:
            return 0
        return sum(self.porcentajes) / len(self.porcentajes)
ca = ControlAsistencia()
print(ca.registrar_porcentajes(80, 95, 110, 70, -5, 100))
print(ca.promedio_asistencia())
