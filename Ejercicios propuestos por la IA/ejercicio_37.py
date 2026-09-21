# Ejercicio 37 - Clasificador de precios
class ClasificadorPrecios:
    def __init__(self):
        self.grupos = {"economico": [], "normal": [],"costoso": []}
    def clasificar_precio(self, precio):
        if precio < 20:
            return "economico"
        elif precio <= 50:
            return "normal"
        else:
            return "costoso"
    def agrupar_precios(self, *precios):
        self.grupos = {"economico": [],"normal": [],"costoso": []}
        for precio in precios:
            categoria = self.clasificar_precio(precio)
            self.grupos[categoria].append(precio)
        return self.grupos
    def promedio_categoria(self, categoria):
        precios = self.grupos[categoria]
        if len(precios) == 0:
            return 0
        return sum(precios) / len(precios)
cp = ClasificadorPrecios()
print(cp.agrupar_precios(10, 25, 60, 45, 15, 80))
print(cp.promedio_categoria("normal"))
