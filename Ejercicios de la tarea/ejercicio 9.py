#Ejercicio 9 - Validador de caracteres
class AnalizadorString():
    def __init__(self):
        self.texto_mas_largo=""

    def solo_vocales(self, letra):
        vocales="aeiouAEIOU"
        if letra in vocales:
            return True
        return False

    def contar_por_tipo(self, texto):
        if len(texto)>len(self.texto_mas_largo):
            self.texto_mas_largo=texto
        resultado={"vocales":[],"consonantes":[],"digitos":[]}
        for caracter in texto:
            if caracter.isdigit():
                resultado["digitos"]+=1
            elif caracter.isalpha():
                if self.solo_vocales(caracter):
                    resultado["vocales"]+=1
                else:
                    resultado["consonantes"]+=1
        return resultado
# Programa principal

astr = AnalizadorString()

print(astr.contar_por_tipo("Hola123"))
print(astr.texto_mas_largo)