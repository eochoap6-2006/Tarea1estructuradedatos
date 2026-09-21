#Ejercicio 19 - Inventario de productos
class Inventario:
    def __init__(self):
        self.productos = {}
    def agregar_stock(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad
    def restar_stock(self, producto, cantidad):
        if producto not in self.productos:
            return False
        if self.productos[producto] >= cantidad:
            self.productos[producto] -= cantidad
            return True
        return False
    def productos_bajo_stock(self, minimo):
        bajos = []
        for producto, cantidad in self.productos.items():
            if cantidad < minimo:
                bajos.append(producto)
        return bajos
inv = Inventario()
inv.agregar_stock("pan", 50)
inv.agregar_stock("leche", 10)
print(inv.restar_stock("pan", 30))
print(inv.productos)
print(inv.productos_bajo_stock(15))