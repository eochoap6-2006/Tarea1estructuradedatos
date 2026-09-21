#Ejercicio 13 - Combinador de listas
class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        mayor = max(len(lista1), len(lista2))
        for i in range(mayor):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado
    def intercalar_multiples(self, *listas):
        if len(listas) == 0:
            return []
        resultado = listas[0]
        for i in range(1, len(listas)):
            resultado = self.intercalar(resultado, listas[i])
        return resultado
cl = CombinadorListas()
print(cl.intercalar([1, 2], [3, 4]))
print(cl.intercalar_multiples([1, 2],[3, 4],[5, 6]))