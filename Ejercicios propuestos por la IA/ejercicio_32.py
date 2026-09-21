# Ejercicio 32 - Generador de intervalos
class GeneradorIntervalos:
    def crear_intervalo(self, inicio, fin):
        numeros = []
        for numero in range(inicio, fin + 1):
            numeros.append(numero)
        return tuple(numeros)
    def combinar_intervalos(self, *intervalos):
        elementos = set()
        for intervalo in intervalos:
            inicio = intervalo[0]
            fin = intervalo[1]
            numeros = self.crear_intervalo(inicio, fin)
            for numero in numeros:
                elementos.add(numero)
        return sorted(list(elementos))
gi = GeneradorIntervalos()
print(gi.crear_intervalo(2, 5))
print(gi.combinar_intervalos((1, 4), (3, 6), (8, 10)))
