#Ejercicio 4 - Inversor de secuencias
class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida=[]
        for i in range(len(lista)-1,-1,-1):
            invertida.append(lista[i])
        return invertida

    def invertir_listas(self, *listas):
        resultado={}
        for lista in listas:
            original=tuple(lista)
            resultado[original]=self.invertir_lista(lista)
        return resultado
inv=InversorSecuencia()
print(inv.invertir_lista([1, 2, 3]))
print(
    inv.invertir_listas(
        [1, 2, 3],
        [4, 5, 6]
    )
)
    


    