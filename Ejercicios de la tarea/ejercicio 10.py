#Ejercicio 10 - Gestor de tareas con prioridad
class Tareas:
    def __init__(self):
        self.tareas=[]

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion,prioridad))

    def tareas_prioritarias(self):
        prioritarias=[]
        for tarea in self.tareas:
            if tarea[1]=="alta":
                prioritarias.append(tarea)
        return prioritarias
    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0]==descripcion:
                self.tareas.remove(tarea)
                return True
        return False


# Programa principal

t = Tareas()

t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
t.agregar_tarea("Hacer deberes", "alta")

print(t.tareas_prioritarias())

t.eliminar_completada("Leer")

print(t.tareas)