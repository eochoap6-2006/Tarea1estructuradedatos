# Ejercicio 26 - Registro de humedad
class ControlHumedad:
    def __init__(self):
        self.humedades = []
    def registrar_humedad(self, valor):
        self.humedades.append(valor)
    def registrar_varias(self, *valores):
        for valor in valores:
            self.registrar_humedad(valor)
    def humedad_minima(self):
        if len(self.humedades) == 0:
            return None
        return min(self.humedades)
    def humedad_maxima(self):
        if len(self.humedades) == 0:
            return None
        return max(self.humedades)
    def humedad_promedio(self):
        if len(self.humedades) == 0:
            return 0
        return sum(self.humedades) / len(self.humedades)
ch = ControlHumedad()
ch.registrar_varias(60, 75, 55, 80, 70)
print(ch.humedad_minima())
print(ch.humedad_maxima())
print(ch.humedad_promedio())
