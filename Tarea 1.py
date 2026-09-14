#Tarea 1
#Erick Ochoa
#Ingenieria en software-3er Semestre
#Materia:Estructuras de datos
#Ejercicio 1
#Validador de notas con promedio
# 1. ENTENDER EL PROBLEMA
# Entrada:
# Varias notas.
# Proceso:
# Validar que cada nota esté entre 0 y 100.
# Guardar solamente las notas válidas.
# Calcular el promedio de las notas guardadas.
# Salida:
# Mostrar las notas válidas y su promedio.
# 2. BOSQUEJO A MANO
# Notas:
# 85, 92, 110, 78, -5, 88
# 85  -> válida
# 92  -> válida
# 110 -> inválida
# 78  -> válida
# -5  -> inválida
# 88  -> válida
# Notas válidas:
# [85, 92, 78, 88]
# Promedio:
# (85 + 92 + 78 + 88) / 4
# 3. DESCUBRIR EL PATRÓN
# El patrón es:
# RECIBIR -> VALIDAR -> GUARDAR -> CALCULAR -> MOSTRAR
# self.notas almacena las notas.
# *args permite recibir varios valores.
# sum() suma los elementos.
# len() cuenta los elementos.
# 4. ESCRIBIR EL CÓDIGO
class Calificador:
    def __init__(self):
        self.notas = []
    def validar_nota(self, nota):
        if 0 <= nota <= 100:
            return True
        else:
            return False
    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas
    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
c = Calificador()
print(c.cargar_notas(85, 92, 110, 78, -5, 88))
print(c.promedio())

#Ejercicio 2
#Contador de palabras únicas
# 1. ENTENDER EL PROBLEMA
# Entrada:
# Varias palabras.
# Proceso:
# Guardar las palabras sin repetir.
# También conservar el orden en el que aparecieron.
# Salida:
# Mostrar:
# - palabras únicas
# - palabras en orden
# - cantidad de palabras diferentes
# 2. BOSQUEJO A MANO
# Palabras:
# hola, mundo, hola
# Únicas:
# hola, mundo
# Cantidad:
# 2
# 3. DESCUBRIR EL PATRÓN
# RECIBIR -> COMPROBAR -> GUARDAR -> CONTAR
# set() no permite duplicados.
# La lista conserva el orden.
# *args permite recibir varias palabras.
# 4. ESCRIBIR EL CÓDIGO
class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas = set()
        self.orden_palabras = []
    def agregar_palabra(self, palabra):
        self.palabras_unicas.add(palabra)
        if palabra not in self.orden_palabras:
            self.orden_palabras.append(palabra)
    def contar_palabras(self):
        return len(self.palabras_unicas)
    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)
at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")
print(at.palabras_unicas)
print(at.orden_palabras)
print(at.contar_palabras())

#Ejercicio 3
#Gestor de compras con totales
# 1. ENTENDER EL PROBLEMA
# Entrada:
# nombre del artículo
# precio del artículo
# Proceso:
# Guardar los artículos en un diccionario.
# Sumar los precios.
# Buscar artículos dentro de un rango de precios.
# Salida:
# Total de la compra.
# Artículos que estén dentro del rango.
# 2. BOSQUEJO A MANO
# pan   = 2.50
# leche = 3.00
# arroz = 5.50
# Total:
# 2.50 + 3.00 + 5.50 = 11.00
# Entre 2 y 4:
# pan
# leche
# 3. DESCUBRIR EL PATRÓN
# GUARDAR -> RECORRER -> FILTRAR -> SUMAR
# El diccionario relaciona:
# nombre -> precio
# .values() obtiene los precios.
# .items() obtiene nombre y precio.
# 4. ESCRIBIR EL CÓDIGO
class CarroCompras:
    def __init__(self):
        self.articulos = {}
    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio
    def total_carrito(self):
        return sum(self.articulos.values())
    def articulos_por_rango(self, precio_min, precio_max):
        encontrados = []
        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                encontrados.append(nombre)
        return encontrados
c = CarroCompras()
c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)
c.agregar_articulo("arroz", 5.50)
print(c.total_carrito())
print(c.articulos_por_rango(2, 4))

#Ejercicio 4
#Inversor de secuencias
# 1. ENTENDER EL PROBLEMA
# Entrada:
# Una o varias listas.
# Proceso:
# Recorrer cada lista desde el final hasta el inicio.
# Salida:
# Mostrar las listas invertidas.
# 2. BOSQUEJO A MANO
# Lista:
# [1, 2, 3]
# Recorrer:
# 3, 2, 1
# Resultado:
# [3, 2, 1]
# 3. DESCUBRIR EL PATRÓN
# RECIBIR -> RECORRER HACIA ATRÁS -> GUARDAR
# range(len(lista)-1, -1, -1)
# empieza en la última posición.
# 4. ESCRIBIR EL CÓDIGO
class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida
    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            original = tuple(lista)
            resultado[original] = self.invertir_lista(lista)
        return resultado
inv = InversorSecuencia()
print(inv.invertir_lista([1, 2, 3]))
print(
    inv.invertir_multiples(
        [1, 2, 3],
        [4, 5, 6]
    )
)

#Ejercicio 5
#Detector de números pares e impares
# 1. ENTENDER EL PROBLEMA
# Entrada:
# Varios números.
# Proceso:
# Comprobar cada número.
# numero % 2 == 0 -> par
# caso contrario -> impar
# Salida:
# Lista de pares.
# Lista de impares.
# Cantidad de cada uno.
# 2. BOSQUEJO A MANO
# 1, 2, 3, 4, 5
# pares:
# 2, 4
# impares:
# 1, 3, 5
# cantidades:
# 2 pares
# 3 impares
# 3. DESCUBRIR EL PATRÓN
# RECORRER -> COMPROBAR -> CLASIFICAR -> CONTAR
# 4. ESCRIBIR EL CÓDIGO
class AnalizadorNumeros:
    def __init__(self):
        self.resultado = {
            "pares": [],
            "impares": []
        }
    def es_par(self, numero):
        return numero % 2 == 0
    def separar(self, *numeros):
        self.resultado = {
            "pares": [],
            "impares": []
        }
        for numero in numeros:
            if self.es_par(numero):
                self.resultado["pares"].append(numero)
            else:
                self.resultado["impares"].append(numero)
        return self.resultado
    def cantidad_pares_impares(self):
        cantidad_pares = len(self.resultado["pares"])
        cantidad_impares = len(self.resultado["impares"])
        return cantidad_pares, cantidad_impares
an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares())

#Ejercicio 6
#Estadísticas de temperatura
# 1. ENTENDER EL PROBLEMA
# Entrada:
# Varias temperaturas.
# Proceso:
# Guardarlas y calcular:
# mínima
# máxima
# promedio
# Salida:
# Mostrar esos tres valores.
# 2. BOSQUEJO A MANO
# 20, 25, 18, 30
# mínima = 18
# máxima = 30
# promedio:
# (20 + 25 + 18 + 30) / 4
# 3. DESCUBRIR EL PATRÓN
# GUARDAR -> BUSCAR MÍNIMO ->
# BUSCAR MÁXIMO -> CALCULAR PROMEDIO
# 4. ESCRIBIR EL CÓDIGO
class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []
    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)
    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)
    def minima(self):
        if len(self.temperaturas) == 0:
            return None
        return min(self.temperaturas)
    def maxima(self):
        if len(self.temperaturas) == 0:
            return None
        return max(self.temperaturas)
    def promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)
gt = GestorTemperatura()
gt.registrar_multiples(20, 25, 18, 30)
print(gt.minima())
print(gt.maxima())
print(gt.promedio())

#Ejercicio 7
#Mapeador de edades
# 1. ENTENDER EL PROBLEMA
# Entrada:
# nombre
# edad
# Proceso:
# Guardar nombre -> edad.
# Buscar personas mayores o iguales a cierta edad.
# Calcular el promedio de edades.
# Salida:
# Personas mayores.
# Edad promedio.
# 2. BOSQUEJO A MANO
# Ana = 28
# Bob = 17
# Carlos = 40
# Mayores de 18:
# Ana
# Carlos
# 3. DESCUBRIR EL PATRÓN
# GUARDAR EN DICCIONARIO ->
# RECORRER -> FILTRAR -> CALCULAR
# 4. ESCRIBIR EL CÓDIGO
class GestorPersonas:
    def __init__(self):
        self.personas = {}
    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad
    def personas_mayores(self, edad_minima):
        mayores = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                mayores.append(nombre)
        return mayores
    def edad_promedio(self):
        if len(self.personas) == 0:
            return 0
        return sum(self.personas.values()) / len(self.personas)
gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
gp.agregar_persona("Carlos", 40)
print(gp.personas_mayores(18))
print(gp.edad_promedio())

#Ejercicio 8
#Asignador de equipos
# 1. ENTENDER EL PROBLEMA
# Entrada:
# nombre del equipo
# jugadores
# Proceso:
# Crear equipos.
# Agregar jugadores.
# Buscar cuál tiene más integrantes.
# Salida:
# Equipos con sus jugadores.
# Equipo con más integrantes.
# 2. BOSQUEJO A MANO
# Equipo A:
# Juan, Pedro
# Equipo B:
# Carlos
# A tiene 2
# B tiene 1
# Mayor:
# A
# 3. DESCUBRIR EL PATRÓN
# CREAR -> AGREGAR ->
# RECORRER -> COMPARAR -> GUARDAR CAMPEÓN
# 4. ESCRIBIR EL CÓDIGO
class Equipos:
    def __init__(self):
        self.equipos = {}
    def crear_equipo(self, nombre_equipo):
        if nombre_equipo not in self.equipos:
            self.equipos[nombre_equipo] = []
    def agregar_jugador(self, equipo, jugador):
        if equipo in self.equipos:
            self.equipos[equipo].append(jugador)
    def equipo_mayor_integrantes(self):
        if len(self.equipos) == 0:
            return None
        equipo_mayor = None
        mayor_cantidad = -1
        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > mayor_cantidad:
                mayor_cantidad = len(jugadores)
                equipo_mayor = equipo
        return equipo_mayor
eq = Equipos()
eq.crear_equipo("A")
eq.crear_equipo("B")
eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")
eq.agregar_jugador("B", "Carlos")
print(eq.equipos)
print(eq.equipo_mayor_integrantes())

#Ejercicio 9
#Validador de caracteres
# 1. ENTENDER EL PROBLEMA
# Entrada:
# Un texto.
# Proceso:
# Contar:
# vocales
# consonantes
# dígitos
# Guardar además el texto más largo analizado.
# Salida:
# Diccionario con las cantidades.
# 2. BOSQUEJO A MANO
# "Hola123"
# Vocales:
# o, a = 2
# Consonantes:
# H, l = 2
# Dígitos:
# 1, 2, 3 = 3
# 3. DESCUBRIR EL PATRÓN
# RECORRER CARACTERES ->
# IDENTIFICAR TIPO ->
# CONTAR
# 4. ESCRIBIR EL CÓDIGO
class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""
    def solo_vocales(self, letra):
        vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
        return letra in vocales
    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
        resultado = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }
        for caracter in texto:
            if caracter.isdigit():
                resultado["digitos"] += 1
            elif caracter.isalpha():
                if self.solo_vocales(caracter):
                    resultado["vocales"] += 1
                else:
                    resultado["consonantes"] += 1
        return resultado
astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))
print(astr.texto_mas_largo)

#Ejercicio 10
#Gestor de tareas con prioridad
# 1. ENTENDER EL PROBLEMA
# Entrada:
# descripción
# prioridad
# Proceso:
# Guardar tareas como tuplas.
# Buscar tareas de prioridad alta.
# Eliminar una tarea completada.
# Salida:
# Tareas prioritarias y lista actualizada.
# 2. BOSQUEJO A MANO
# ("Estudiar", "alta")
# ("Leer", "baja")
# ("Hacer deberes", "alta")
# Prioritarias:
# Estudiar
# Hacer deberes
# 3. DESCUBRIR EL PATRÓN
# GUARDAR -> RECORRER ->
# FILTRAR -> ELIMINAR
# 4. ESCRIBIR EL CÓDIGO
class Tareas:
    def __init__(self):
        self.tareas = []
    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append(
            (descripcion, prioridad)
        )
    def tareas_prioritarias(self):
        prioritarias = []
        for tarea in self.tareas:
            if tarea[1] == "alta":
                prioritarias.append(tarea)
        return prioritarias
    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                return True
        return False
t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
t.agregar_tarea("Hacer deberes", "alta")
print(t.tareas_prioritarias())
t.eliminar_completada("Leer")
print(t.tareas)

#Ejercicio 11
#Contador de frecuencia
# 1. ENTENDER EL PROBLEMA
# Entrada:
# Elementos.
# Proceso:
# Contar cuántas veces aparece cada uno.
# Encontrar el más frecuente.
# Salida:
# Diccionario de frecuencias.
# Elemento más frecuente.
# Frecuencia de un elemento.
# 2. BOSQUEJO A MANO
# a
# b
# a
# a = 2
# b = 1
# Más frecuente:
# a
# 3. DESCUBRIR EL PATRÓN
# RECIBIR -> COMPROBAR SI EXISTE ->
# AUMENTAR CONTADOR -> BUSCAR MAYOR
# 4. ESCRIBIR EL CÓDIGO
class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}
    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1
    def elemento_mas_frecuente(self):
        if len(self.frecuencias) == 0:
            return None
        mayor_elemento = None
        mayor_frecuencia = 0
        for elemento, frecuencia in self.frecuencias.items():
            if frecuencia > mayor_frecuencia:
                mayor_frecuencia = frecuencia
                mayor_elemento = elemento
        return mayor_elemento
    def frecuencia_elemento(self, elemento):
        if elemento in self.frecuencias:
            return self.frecuencias[elemento]
        return 0
cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print(cf.frecuencias)
print(cf.elemento_mas_frecuente())
print(cf.frecuencia_elemento("a"))

#Ejercicio 12
#Selector de rango con tuplas
# 1. ENTENDER EL PROBLEMA
# Entrada:
# inicio y fin de uno o varios rangos.
# Proceso:
# Crear los números del rango.
# Unir varios rangos evitando duplicados.
# Salida:
# Tupla del rango.
# Lista ordenada de valores únicos.
# 2. BOSQUEJO A MANO
# rango 1:
# 1, 2, 3
# rango 2:
# 2, 3, 4
# unión:
# 1, 2, 3, 4
# 3. DESCUBRIR EL PATRÓN
# CREAR RANGO -> AGREGAR A SET ->
# ELIMINAR DUPLICADOS -> ORDENAR
# 4. ESCRIBIR EL CÓDIGO
class SelectorRango:
    def crear_rango(self, inicio, fin):
        numeros = []
        for numero in range(inicio, fin + 1):
            numeros.append(numero)
        return tuple(numeros)
    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()
        for rango in rangos:
            inicio = rango[0]
            fin = rango[1]
            numeros = self.crear_rango(inicio, fin)
            for numero in numeros:
                elementos.add(numero)
        return sorted(list(elementos))
sr = SelectorRango()
print(sr.crear_rango(1, 3))
print(
    sr.elementos_en_multiples_rangos(
        (1, 3),
        (2, 4)
    )
)

#Ejercicio 13
#Combinador de listas
# 1. ENTENDER EL PROBLEMA
# Entrada:
# Dos o más listas.
# Proceso:
# Tomar un elemento de una lista,
# luego uno de la otra.
# Salida:
# Una lista intercalada.
# 2. BOSQUEJO A MANO
# lista1 = [1, 2]
# lista2 = [3, 4]
# resultado:
# 1
# 3
# 2
# 4
# [1, 3, 2, 4]
# 3. DESCUBRIR EL PATRÓN
# RECORRER POR POSICIÓN ->
# AGREGAR DE LISTA 1 ->
# AGREGAR DE LISTA 2
# 4. ESCRIBIR EL CÓDIGO
class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        mayor = max(len(lista1), len(lista2))
        for i in range(mayor):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado
    def intercalar_multiples(self, *listas):
        if len(listas) == 0:
            return []
        resultado = listas[0]
        for i in range(1, len(listas)):
            resultado = self.intercalar(
                resultado,
                listas[i]
            )
        return resultado
cl = CombinadorListas()
print(cl.intercalar([1, 2], [3, 4]))
print(
    cl.intercalar_multiples(
        [1, 2],
        [3, 4],
        [5, 6]
    )
)

#Ejercicio 14
#Mapeo de estudiantes a notas
# 1. ENTENDER EL PROBLEMA
# Entrada:
# estudiante
# nota
# Proceso:
# Guardar estudiante -> nota.
# Buscar aprobados.
# Buscar la nota más alta.
# Salida:
# Lista de aprobados.
# Mejor estudiante.
# 2. BOSQUEJO A MANO
# Ana = 95
# Bob = 70
# Carlos = 88
# Aprobados con mínimo 70:
# Ana, Bob, Carlos
# Mejor:
# Ana = 95
# 3. DESCUBRIR EL PATRÓN
# GUARDAR -> FILTRAR ->
# COMPARAR -> GUARDAR CAMPEÓN
# 4. ESCRIBIR EL CÓDIGO
class RegistroNotas:
    def __init__(self):
        self.notas = {}
    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota
    def estudiantes_aprobados(self, nota_minima):
        aprobados = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)
        return aprobados
    def mejor_estudiante(self):
        if len(self.notas) == 0:
            return None
        mejor_nombre = None
        mejor_nota = float("-inf")
        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante
        return mejor_nombre, mejor_nota
rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
rn.registrar("Carlos", 88)
print(rn.estudiantes_aprobados(70))
print(rn.mejor_estudiante())

#Ejercicio 15
#Divisores de un número
# 1. ENTENDER EL PROBLEMA
# Entrada:
# numero
# Proceso:
# Probar divisores desde 1 hasta el número.
# Si:
# numero % i == 0
# entonces i es divisor.
# También comprobar si el número es perfecto.
# Salida:
# Divisores.
# True o False si es perfecto.
# 2. BOSQUEJO A MANO
# numero = 6
# divisores:
# 1, 2, 3, 6
# Divisores propios:
# 1 + 2 + 3 = 6
# Entonces:
# 6 es perfecto.
# 3. DESCUBRIR EL PATRÓN
# RECORRER -> COMPROBAR RESIDUO ->
# GUARDAR DIVISORES -> SUMAR
# 4. ESCRIBIR EL CÓDIGO
class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)
    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma = 0
        for divisor in divisores:
            if divisor != numero:
                suma += divisor
        return suma == numero
    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(
                numero
            )
        return resultado
df = DivisorFinder()
print(df.encontrar_divisores(12))
print(df.es_perfecto(6))
print(df.encontrar_multiples_divisores(6, 10, 12))

#Ejercicio 16
#Codificador César
# 1. ENTENDER EL PROBLEMA
# Entrada:
# palabra
# desplazamiento
# Proceso:
# Cambiar cada letra cierta cantidad
# de posiciones en el alfabeto.
# Salida:
# Palabra codificada.
# 2. BOSQUEJO A MANO
# palabra = "hola"
# desplazamiento = 3
# h -> k
# o -> r
# l -> o
# a -> d
# resultado:
# krod
# 3. DESCUBRIR EL PATRÓN
# RECORRER LETRAS ->
# CONVERTIR LETRA A NÚMERO ->
# SUMAR DESPLAZAMIENTO ->
# CONVERTIR A LETRA
# ord() convierte carácter a número.
# chr() convierte número a carácter.
# % 26 permite regresar al inicio
# después de la z.
# 4. ESCRIBIR EL CÓDIGO
class CodificadorCesar:
    def __init__(self):
        self.historial = {}
    def codificar_letra(self, letra, desplazamiento):
        if "a" <= letra <= "z":
            posicion = ord(letra) - ord("a")
            nueva_posicion = (
                posicion + desplazamiento
            ) % 26
            return chr(
                nueva_posicion + ord("a")
            )
        elif "A" <= letra <= "Z":
            posicion = ord(letra) - ord("A")
            nueva_posicion = (
                posicion + desplazamiento
            ) % 26
            return chr(
                nueva_posicion + ord("A")
            )
        else:
            return letra
    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            resultado += self.codificar_letra(
                letra,
                desplazamiento
            )
        self.historial[
            (palabra, desplazamiento)
        ] = resultado
        return resultado
cc = CodificadorCesar()
print(cc.codificar_palabra("hola", 3))
print(cc.historial)

#Ejercicio 17
#Grupo de edades
# 1. ENTENDER EL PROBLEMA
# Entrada:
# Varias edades.
# Proceso:
# Clasificarlas en:
# niño
# adolescente
# adulto
# mayor
# También calcular el promedio
# de una categoría.
# Salida:
# Diccionario de grupos.
# Promedio de una categoría.
# 2. BOSQUEJO A MANO
# 5  -> niño
# 15 -> adolescente
# 30 -> adulto
# 70 -> mayor
# 3. DESCUBRIR EL PATRÓN
# RECIBIR -> CLASIFICAR ->
# GUARDAR EN GRUPO -> CALCULAR
# 4. ESCRIBIR EL CÓDIGO
class AgrupadorEdades:
    def __init__(self):

        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }
    def clasificar_edad(self, edad):
        if edad <= 12:
            return "niño"

        elif edad <= 17:
            return "adolescente"
        elif edad <= 64:
            return "adulto"
        else:
            return "mayor"
    def agrupar_por_categoria(self, *edades):
        self.grupos = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)
        return self.grupos
    def edad_promedio_categoria(self, categoria):
        edades = self.grupos[categoria]
        if len(edades) == 0:
            return 0
        return sum(edades) / len(edades)
ae = AgrupadorEdades()
print(
    ae.agrupar_por_categoria(
        5, 15, 30, 70
    )
)
print(
    ae.edad_promedio_categoria("adulto")
)

#Ejercicio 18
#Matriz de distancias
# 1. ENTENDER EL PROBLEMA

# Entrada:
# Dos puntos:
#
# p1 = (x1, y1)
# p2 = (x2, y2)
# Proceso:
# Calcular la distancia euclidiana.
# También buscar cuál punto está
# más cerca de un punto de referencia.
# Salida:
# Distancia.
# Punto más cercano.
# 2. BOSQUEJO A MANO
# p1 = (0, 0)
# p2 = (3, 4)
# diferencia x = 3
# diferencia y = 4
# 3² + 4²
# 9 + 16
# 25
# raíz de 25 = 5
# 3. DESCUBRIR EL PATRÓN
# RECIBIR COORDENADAS ->
# CALCULAR DIFERENCIAS ->
# ELEVAR AL CUADRADO ->
# SUMAR -> SACAR RAÍZ
# 4. ESCRIBIR EL CÓDIGO
class CalculadorDistancia:
    def __init__(self):
        self.distancias = []
    def distancia_euclidiana(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        distancia = (
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        ) ** 0.5
        self.distancias.append(distancia)
        return distancia
    def punto_mas_cercano(self, referencia, *puntos):
        if len(puntos) == 0:
            return None
        cercano = None
        menor_distancia = None
        for punto in puntos:
            distancia = self.distancia_euclidiana(
                referencia,
                punto
            )
            if (
                menor_distancia is None
                or distancia < menor_distancia
            ):
                menor_distancia = distancia
                cercano = punto
        return cercano
cd = CalculadorDistancia()
print(
    cd.distancia_euclidiana(
        (0, 0),
        (3, 4)
    )
)
print(
    cd.punto_mas_cercano(
        (0, 0),
        (5, 5),
        (1, 1),
        (10, 10)
    )
)
print(cd.distancias)

#Ejercicio 19
#Inventario de productos
# 1. ENTENDER EL PROBLEMA
# Entrada:
# producto
# cantidad
# Proceso:
# Agregar stock.
# Restar stock.
# Buscar productos con pocas unidades.
# Salida:
# Inventario actualizado.
# Productos bajo stock.
# 2. BOSQUEJO A MANO
# pan = 50
# leche = 10
# vender 30 panes
# pan:
# 50 - 30 = 20
# mínimo = 15
# leche tiene 10
# entonces está bajo stock.
# 3. DESCUBRIR EL PATRÓN
# GUARDAR -> SUMAR STOCK ->
# COMPROBAR DISPONIBILIDAD ->
# RESTAR -> FILTRAR
# 4. ESCRIBIR EL CÓDIGO
class Inventario:
    def __init__(self):
        self.productos = {}
    def agregar_stock(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad
    def restar_stock(self, producto, cantidad):
        if producto not in self.productos:
            return False
        if self.productos[producto] >= cantidad:
            self.productos[producto] -= cantidad
            return True
        return False
    def productos_bajo_stock(self, minimo):
        bajos = []
        for producto, cantidad in self.productos.items():
            if cantidad < minimo:
                bajos.append(producto)
        return bajos
inv = Inventario()
inv.agregar_stock("pan", 50)
inv.agregar_stock("leche", 10)
print(inv.restar_stock("pan", 30))
print(inv.productos)
print(inv.productos_bajo_stock(15))

#Ejercicio 20
#Analizador de patrones en textos
# 1. ENTENDER EL PROBLEMA
# Entrada:
# texto
# patrón
# Proceso:
# Separar el texto en palabras.
# Buscar palabras que comiencen
# con determinado patrón.
# También agrupar palabras
# según su longitud.
# Finalmente obtener las palabras únicas.
# Salida:
# Palabras encontradas.
# Diccionario agrupado por longitud.
# Palabras únicas.
# 2. BOSQUEJO A MANO
# texto:
# "el gato grande juega"
# patrón:
# "g"
# empiezan con g:
# gato
# grande
# Resultado:
# ["gato", "grande"]
# 3. DESCUBRIR EL PATRÓN
# SEPARAR TEXTO ->
# RECORRER PALABRAS ->
# COMPROBAR PATRÓN ->
# AGRUPAR -> ELIMINAR DUPLICADOS
# .split()
# separa palabras.
# .startswith()
# comprueba cómo empieza una palabra.
# set()
# elimina duplicados.
# 4. ESCRIBIR EL CÓDIGO
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
    ap.encontrar_palabras(
        "el gato grande juega",
        "g"
    )
)
print(
    ap.agrupar_por_longitud(
        "el gato está aquí"
    )
)
print(ap.palabras_unicas())