#Ejercicio 2 - Contador de palabras únicas
class Analizadordetexto:
    def __init__(self):
        self.palabras_unicas=set()
        self.orden_palabras=[]

    def agregar_palabra(self , palabra):
        self.palabras_unicas.add(palabra)
        if palabra not in self.orden_palabras:
            self.orden_palabras.append(palabra)

    def agregar_multiples(self, *args):

        for palabra in args:
            self.agregar_palabra(palabra)
        return self.orden_palabras 

    def contar_palabra (self):
        return len(self.palabras_unicas)

at=Analizadordetexto()
print(at.agregar_multiples("hola","mundo","hola"))
print(at.contar_palabra())        

    