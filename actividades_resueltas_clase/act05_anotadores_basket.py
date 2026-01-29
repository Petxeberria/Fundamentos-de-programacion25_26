# Listas vacias de jugadores/anotaciones
lista_anotaciones = []
lista_jugadores = []
max_anotacion = 0
nombre_maxima_anotacion = ""

for jugador in range(3):
    # Pedir el jugador y las anotaciones
    nombre_jugador = input(f"Introduce el nombre del jugador num {jugador}: ")
    anotacion_jugador = int(input(f"Anotacion del jugador num {jugador}: "))

    # Anyadir a las listas
    lista_anotaciones.append(anotacion_jugador)
    lista_jugadores.append(nombre_jugador)

    # Calcular el maximo anotador
    if anotacion_jugador > max_anotacion:
        maxima_anotacion = anotacion_jugador
        nombre_maxima_anotacion = nombre_jugador

# Resultados finales
for jugador in range(3):
    print(f"Jugador {lista_jugadores[jugador]} ha anotado {lista_anotaciones[jugador]} ptos")

print(f"La maxima anotacion ha sido {maxima_anotacion}")
print(f"Del jugador {nombre_maxima_anotacion}")
