# Ejercicio 31 - Contador de votos
class ContadorVotos:
    def __init__(self):
        self.votos = {}
    def agregar_voto(self, candidato):
        if candidato in self.votos:
            self.votos[candidato] += 1
        else:
            self.votos[candidato] = 1
    def candidato_mas_votado(self):
        if len(self.votos) == 0:
            return None
        mejor_candidato = None
        mayor_cantidad = 0
        for candidato, cantidad in self.votos.items():
            if cantidad > mayor_cantidad:
                mayor_cantidad = cantidad
                mejor_candidato = candidato
        return mejor_candidato
    def votos_de(self, candidato):
        if candidato in self.votos:
            return self.votos[candidato]
        return 0
cv = ContadorVotos()
cv.agregar_voto("Ana")
cv.agregar_voto("Luis")
cv.agregar_voto("Ana")
cv.agregar_voto("Ana")

print(cv.votos)
print(cv.candidato_mas_votado())
print(cv.votos_de("Ana"))
