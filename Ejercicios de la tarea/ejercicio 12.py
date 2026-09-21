#Ejercicio 12 - Selector de rango con tuplas
class SelectorRango:
    def crear_rango(self, inicio, fin):
        numeros = []
        for numero in range(inicio, fin + 1):
            numeros.append(numero)
        return tuple(numeros)
    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()
        for rango in rangos:
            inicio = rango[0]
            fin = rango[1]
            numeros = self.crear_rango(inicio, fin)
            for numero in numeros:
                elementos.add(numero)
        return sorted(list(elementos))
sr = SelectorRango()
print(sr.crear_rango(1, 3))
print(sr.elementos_en_multiples_rangos((1, 3),(2, 4)))