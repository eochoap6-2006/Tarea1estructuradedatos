#Ejercicio 20 - Analizador de patrones en textos
class AnalizadorPatrones:
    def __init__(self):
        self.ultimo_texto = ""
    def encontrar_palabras(self, texto, patron):
        self.ultimo_texto = texto
        palabras = texto.split()
        encontradas = []
        for palabra in palabras:
            if palabra.startswith(patron):
                encontradas.append(palabra)
        return encontradas
    def agrupar_por_longitud(self, texto):
        self.ultimo_texto = texto
        palabras = texto.split()
        grupos = {}
        for palabra in palabras:
            longitud = len(palabra)
            if longitud not in grupos:
                grupos[longitud] = []
            grupos[longitud].append(palabra)
        return grupos
    def palabras_unicas(self):
        palabras = self.ultimo_texto.split()
        return set(palabras)
ap = AnalizadorPatrones()
print(
    ap.encontrar_palabras("el gato grande juega", "g")
)
print(
    ap.agrupar_por_longitud("el gato está aquí" )
)
print(ap.palabras_unicas())