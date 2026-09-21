# Ejercicio 24 - Ordenador descendente manual
class OrdenadorNumeros:
    def ordenar_descendente(self, lista):
        copia = lista.copy()

        for i in range(len(copia)):
            for j in range(i + 1, len(copia)):
                if copia[j] > copia[i]:
                    auxiliar = copia[i]
                    copia[i] = copia[j]
                    copia[j] = auxiliar
        return copia
    def ordenar_varias(self, *listas):
        resultado = {}
        for lista in listas:
            clave = tuple(lista)
            resultado[clave] = self.ordenar_descendente(lista)
        return resultado
on = OrdenadorNumeros()
print(on.ordenar_descendente([4, 1, 8, 3]))
print(on.ordenar_varias(
    [4, 1, 8, 3],
    [10, 2, 7]
))
