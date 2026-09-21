# Ejercicio 34 - Registro de puntajes
class RegistroPuntajes:
    def __init__(self):
        self.puntajes = {}
    def registrar(self, jugador, puntos):
        self.puntajes[jugador] = puntos
    def jugadores_superiores(self, puntos_minimos):
        jugadores = []
        for jugador, puntos in self.puntajes.items():
            if puntos >= puntos_minimos:
                jugadores.append(jugador)
        return jugadores
    def mejor_jugador(self):
        if len(self.puntajes) == 0:
            return None
        mejor_nombre = None
        mejor_puntaje = None
        for jugador, puntos in self.puntajes.items():
            if mejor_puntaje is None or puntos > mejor_puntaje:
                mejor_puntaje = puntos
                mejor_nombre = jugador
        return (mejor_nombre, mejor_puntaje)
rp = RegistroPuntajes()
rp.registrar("Juan", 80)
rp.registrar("Ana", 95)
rp.registrar("Pedro", 70)
print(rp.jugadores_superiores(80))
print(rp.mejor_jugador())
