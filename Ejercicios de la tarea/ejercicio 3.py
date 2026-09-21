#Ejercicio 3 - Gestor de compras con totales
class CarroCompras:
    def __init__(self):
        self.articulo={}

    def agregar_articulo(self, nombre, precio):
        self.articulo[nombre]=precio

    def total_carrito(self):
        return sum(self.articulo.values())

    def articlos_por_rango(self , preciomin, preciomax):
        encontrados=[]
        for nombre, precio in self.articulos.items():
            if precio>=preciomin and precio<=preciomax:
                encontrados.append(nombre)
        return encontrados

c = CarroCompras()
c.agregar_articulo("pan",2.50)
c.agregar_articulo("leche",3.00)
print(c.total_carrito())
