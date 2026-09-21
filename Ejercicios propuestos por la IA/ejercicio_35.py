# Ejercicio 35 - Buscador de múltiplos
class BuscadorMultiplos:
    def encontrar_multiplos(self, numero, limite):
        multiplos = []
        for valor in range(numero, limite + 1, numero):
            multiplos.append(valor)
        return tuple(multiplos)
    def es_multiplo(self, numero, divisor):
        if divisor == 0:
            return False
        return numero % divisor == 0
    def multiples_de_varios(self, *numeros):
        resultado = {}
        for numero in numeros:
            multiplos = []
            for i in range(1, 6):
                multiplos.append(numero * i)
            resultado[numero] = tuple(multiplos)
        return resultado
bm = BuscadorMultiplos()
print(bm.encontrar_multiplos(4, 20))
print(bm.es_multiplo(20, 4))
print(bm.multiples_de_varios(2, 3, 5))
