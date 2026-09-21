# Ejercicio 33 - Mezclador de nombres
class MezcladorListas:
    def mezclar(self, lista1, lista2):
        resultado = []
        mayor = max(len(lista1), len(lista2))
        for i in range(mayor):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado
    def mezclar_varias(self, *listas):
        if len(listas) == 0:
            return []
        resultado = listas[0]
        for i in range(1, len(listas)):
            resultado = self.mezclar(resultado, listas[i])
        return resultado
ml = MezcladorListas()
print(ml.mezclar(["Ana", "Luis"],["Pedro", "Maria"]))
print(ml.mezclar_varias(["Ana", "Luis"],["Pedro", "Maria"],["Carlos", "Sofia"]))
