# Ejercicio 38 - Distancia entre ciudades
class MapaCoordenadas:
    def __init__(self):
        self.distancias = []
    def calcular_distancia(self, punto1, punto2):
        x1 = punto1[0]
        y1 = punto1[1]
        x2 = punto2[0]
        y2 = punto2[1]
        distancia = ((x2 - x1) ** 2 +(y2 - y1) ** 2) ** 0.5
        self.distancias.append(distancia)
        return distancia
    def punto_mas_lejano(self, referencia, *puntos):
        if len(puntos) == 0:
            return None
        punto_lejano = None
        mayor_distancia = None
        for punto in puntos:
            distancia = self.calcular_distancia( referencia, punto)
            if mayor_distancia is None or distancia > mayor_distancia:
                mayor_distancia = distancia
                punto_lejano = punto
        return punto_lejano
mc = MapaCoordenadas()
print(mc.calcular_distancia((0, 0), (3, 4)))
print(mc.punto_mas_lejano((0, 0),(1, 1),(5, 5),(2, 2)))
print(mc.distancias)
