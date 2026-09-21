#Ejercicio 17 - Grupo de edades
class AgrupadorEdades:
    def __init__(self):
        self.grupos = {"niño": [],"adolescente": [],"adulto": [],"mayor": []}
    def clasificar_edad(self, edad):
        if edad <= 12:
            return "niño"
        elif edad <= 17:
            return "adolescente"
        elif edad <= 64:
            return "adulto"
        else:
            return "mayor"
    def agrupar_por_categoria(self, *edades):
        self.grupos = {"niño": [],"adolescente": [],"adulto": [],"mayor": []}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)
        return self.grupos
    def edad_promedio_categoria(self, categoria):
        edades = self.grupos[categoria]
        if len(edades) == 0:
            return 0
        return sum(edades) / len(edades)
ae = AgrupadorEdades()
print(ae.agrupar_por_categoria( 5, 15, 30, 70))
print(ae.edad_promedio_categoria("adulto"))