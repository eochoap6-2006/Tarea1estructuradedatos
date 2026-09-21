#Ejercicio 11 - Contador de frecuencia
class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias={}

    def agregar_elemento(self, elemento):
        if elemento in self.elemento:
            self.frecuencias[elemento]+=1
        else:
            self.frecuencias[elemento]=1

    def elemento_mas_frecuente(self):
        if len(self.frecuencias)==0:
            return None
        mayor_elemento=None
        mayor_frecuencia=0
        for elemento, frecuencia in self.frecuencias.items():
            if frecuencia>mayor_frecuencia:
                mayor_frecuencia=frecuencia
                mayor_elemento=elemento
        return mayor_elemento

    def frecuencia_elemento(self ,elemento):
        if elemento in self.frecuencias:
            return self.frecuencias[elemento]




# Programa principal
cf= ContadorFrecuencia()

cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")

print(cf.frecuencias)
print(cf.elemento_mas_frecuente())
print(cf.frecuencia_elemento("a"))