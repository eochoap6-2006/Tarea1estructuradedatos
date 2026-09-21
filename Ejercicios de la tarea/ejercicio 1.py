#Ejercicio 1 - Validador de notas con promedio
class Calificador:
    def __init__(self):
        self.notas=[]

    def validar_nota(self, nota):
        if nota>=0 and nota<=100:
            return True
        else:
            return False

    def cargar_notas (self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas
    
    def promedio (self):
        return sum(self.notas)/len(self.notas)

c = Calificador()
print(c.cargar_notas(85, 92, 110, 78, -5, 88))
print (c.promedio())
