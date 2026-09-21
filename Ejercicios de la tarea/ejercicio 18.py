#Ejercicio 18 - Matriz de distancias
class CalculadorDistancia:
    def __init__(self):
        self.distancias = []
    def distancia_euclidiana(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        distancia = ((x2 - x1) ** 2 +(y2 - y1) ** 2) ** 0.5
        self.distancias.append(distancia)
        return distancia
    def punto_mas_cercano(self, referencia, *puntos):
        if len(puntos) == 0:
            return None
        cercano = None
        menor_distancia = None
        for punto in puntos:
            distancia = self.distancia_euclidiana(
                referencia,
                punto
            )
            if (menor_distancia is None or distancia < menor_distancia):
                menor_distancia = distancia
                cercano = punto
        return cercano
cd = CalculadorDistancia()
print(
    cd.distancia_euclidiana(
        (0, 0),
        (3, 4)
    )
)
print(
    cd.punto_mas_cercano(
        (0, 0),
        (5, 5),
        (1, 1),
        (10, 10)
    )
)
print(cd.distancias)