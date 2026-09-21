#Ejercicio 5 - Detector de números pares e impares
class AnalizadorNumeros:
    def __init__(self):
        self.resultado={"Pares":[], "Impares":[]}

    def es_par (self, numero):
        if numero % 2==0:
            return True
        else:
            return False

    def separar(self,*numeros):
        for numero in numeros:
            if self.es_par(numero):
                self.resultado["Pares"].append(numero)
            else:
                self.resultado["Impares"].append(numero)
        return self.resultado
    def cantidad_pares_impares(self):
        cant_pares=len(self.resultado["Pares"])
        cant_impares=len(self.resultado["Impares"])
        return (cant_pares,cant_impares)
# Programa principal

an = AnalizadorNumeros()

print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares())