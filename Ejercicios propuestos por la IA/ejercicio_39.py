# Ejercicio 39 - Control de almacén
class Almacen:
    def __init__(self):
        self.productos = {}
    def ingresar_producto(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad
    def retirar_producto(self, producto, cantidad):
        if producto not in self.productos:
            return False
        if self.productos[producto] >= cantidad:
            self.productos[producto] -= cantidad
            return True
        return False
    def productos_sobre_stock(self, maximo):
        productos = []
        for producto, cantidad in self.productos.items():
            if cantidad > maximo:
                productos.append(producto)
        return productos
a = Almacen()
a.ingresar_producto("arroz", 50)
a.ingresar_producto("leche", 20)
a.ingresar_producto("pan", 70)
print(a.retirar_producto("arroz", 10))
print(a.productos)
print(a.productos_sobre_stock(40))
