# Ejercicio 40 - Analizador de frases
class AnalizadorFrases:
    def buscar_terminacion(self, texto, terminacion):
        palabras = texto.split()
        encontradas = []
        for palabra in palabras:
            if palabra.endswith(terminacion):
                encontradas.append(palabra)
        return encontradas
    def agrupar_por_inicial(self, texto):
        palabras = texto.split()
        grupos = {}
        for palabra in palabras:
            inicial = palabra[0].lower()
            if inicial not in grupos:
                grupos[inicial] = []
            grupos[inicial].append(palabra)
        return grupos
    def obtener_palabras_unicas(self, texto):
        palabras = texto.split()
        return set(palabras)
af = AnalizadorFrases()
texto = "casa carro perro pelota casa"
print(af.buscar_terminacion(texto, "a"))
print(af.agrupar_por_inicial(texto))
print(af.obtener_palabras_unicas(texto))
