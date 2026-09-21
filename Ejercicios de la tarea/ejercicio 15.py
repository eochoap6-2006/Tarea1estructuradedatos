#Ejercicio 15 - Divisores de un número
class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)
    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = 0
        for divisor in divisores:
            if divisor != numero:
                suma += divisor
        return suma == numero
    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado
df = DivisorFinder()
print(df.encontrar_divisores(12))
print(df.es_perfecto(6))
print(df.encontrar_multiples_divisores(6, 10, 12))