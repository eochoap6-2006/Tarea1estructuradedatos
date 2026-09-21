# Ejercicio 22 - Registro de etiquetas únicas
class GestorEtiquetas:
    def __init__(self):
        self.etiquetas_unicas = set()
        self.orden_etiquetas = []
    def agregar_etiqueta(self, etiqueta):
        self.etiquetas_unicas.add(etiqueta)
        if etiqueta not in self.orden_etiquetas:
            self.orden_etiquetas.append(etiqueta)
    def cantidad_etiquetas(self):
        return len(self.etiquetas_unicas)
    def agregar_varias(self, *args):
        for etiqueta in args:
            self.agregar_etiqueta(etiqueta)
ge = GestorEtiquetas()
ge.agregar_varias("python", "clases", "python", "listas")
print(ge.etiquetas_unicas)
print(ge.orden_etiquetas)
print(ge.cantidad_etiquetas())