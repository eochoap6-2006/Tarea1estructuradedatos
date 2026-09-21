#Ejercicio 6 - Estadísticas de temperatura
class GestorTemperatura:
    def __init__(self):
        self.temperatura=[]

    def registrar_temperatura(self, temperatura):
        self.temperatura.append(temperatura)

    def minima(self):
        if len(self.temperatura) == 0:
            return None
        return min(self.temperatura)

    def maxima(self):
        if len(self.temperatura)==0:
            return None
        return max(self.temperatura)

    def promedio(self):
        if len(self.temperatura)==0:
            return 0
        return sum(self.temperatura)/len(self.temperatura)

    def registrar_multiples(self, *temperaturas):
        for temperatura in temperaturas:
            self.registrar_temperatura(temperatura)

# Programa principal

gt = GestorTemperatura()

gt.registrar_multiples(20, 25, 18, 30)

print(gt.minima())
print(gt.maxima())
print(gt.promedio())