#Ejercicio 16 - Codificador/Decodificador
class CodificadorCesar:
    def __init__(self):
        self.historial = {}
    def codificar_letra(self, letra, desplazamiento):
        if letra.islower():
            posicion = ord(letra) - ord("a")
            nueva_posicion = (posicion + desplazamiento) % 26
            return chr(nueva_posicion + ord("a"))
        elif letra.isupper():
            posicion = ord(letra) - ord("A")
            nueva_posicion = (posicion + desplazamiento) % 26
            return chr(nueva_posicion + ord("A"))
        else:
            return letra
    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            resultado += self.codificar_letra(letra,desplazamiento)
        self.historial[(palabra, desplazamiento)] = resultado
        return resultado
cc = CodificadorCesar()
print(cc.codificar_palabra("hola", 3))
print(cc.historial)