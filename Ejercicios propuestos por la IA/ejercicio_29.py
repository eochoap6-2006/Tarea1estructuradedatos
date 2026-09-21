# Ejercicio 29 - Analizador de caracteres
class AnalizadorCaracteres:
    def __init__(self):
        self.texto_mas_corto = None
    def es_mayuscula(self, caracter):
        if caracter.isalpha() and caracter.isupper():
            return True
        return False
    def analizar(self, texto):
        if self.texto_mas_corto is None or len(texto) < len(self.texto_mas_corto):
            self.texto_mas_corto = texto
        resultado = { "mayusculas": 0,  "minusculas": 0, "numeros": 0  }
        for caracter in texto:
            if caracter.isdigit():
                resultado["numeros"] += 1
            elif caracter.isalpha():
                if self.es_mayuscula(caracter):
                    resultado["mayusculas"] += 1
                else:
                    resultado["minusculas"] += 1
        return resultado
ac = AnalizadorCaracteres()
print(ac.analizar("HolaMundo123"))
print(ac.analizar("Python7"))
print(ac.texto_mas_corto)
