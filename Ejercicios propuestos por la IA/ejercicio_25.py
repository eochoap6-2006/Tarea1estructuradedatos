# Ejercicio 25 - Clasificador de positivos y negativos
class ClasificadorNumeros:
    def __init__(self):
        self.resultado = { "positivos": [], "negativos": []}
    def es_positivo(self, numero):
        if numero >= 0:
            return True
        else:
            return False
    def clasificar(self, *numeros):
        self.resultado = {"positivos": [],"negativos": []}
        for numero in numeros:
            if self.es_positivo(numero):
                self.resultado["positivos"].append(numero)
            else:
                self.resultado["negativos"].append(numero)
        return self.resultado
    def cantidad_por_tipo(self):
        cantidad_positivos = len(self.resultado["positivos"])
        cantidad_negativos = len(self.resultado["negativos"])
        return (cantidad_positivos, cantidad_negativos)
cn = ClasificadorNumeros()
print(cn.clasificar(-5, 0, 3, -2, 10, -8))
print(cn.cantidad_por_tipo())
