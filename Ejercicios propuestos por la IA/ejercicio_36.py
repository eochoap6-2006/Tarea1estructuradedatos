# Ejercicio 36 - Codificador de números
class CodificadorDigitos:
    def __init__(self):
        self.historial = {}
    def codificar_digito(self, digito, desplazamiento):
        return (digito + desplazamiento) % 10
    def codificar_numero(self, numero, desplazamiento):
        texto = str(numero)
        resultado = ""
        for caracter in texto:
            digito = int(caracter)
            nuevo_digito = self.codificar_digito(digito,desplazamiento)
            resultado += str(nuevo_digito)
        numero_codificado = int(resultado)
        self.historial[(numero, desplazamiento)] = numero_codificado
        return numero_codificado
cd = CodificadorDigitos()
print(cd.codificar_numero(789, 3))
print(cd.historial)
