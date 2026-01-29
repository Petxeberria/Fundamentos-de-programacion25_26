# Listas
jugadores_basket = []

canastas_1_punto = []
canastas_2_punto = []
canastas_3_punto = []

# Bucle infinito con while
while True:
    nombre_jugador = input("Introduce el nombre del jugador (o 'salir' para finalizar)")
    if nombre_jugador.lower() == "salir":
        break

    # Preguntar por el numero de canastas
    canastas_1 = int(input(f"Introduce el numero de canastas de 1 del jugador {nombre_jugador}:  "))
    canastas_2 = int(input(f"Introduce el numero de canastas de 2 del jugador {nombre_jugador}: "))
    canastas_3 = int(input(f"Introduce el numero de canastas de 3 del jugador {nombre_jugador}: "))

    if canastas_1 >= 0 and canastas_2 >= 0 and canastas_3 >= 0:
        canastas_1_punto.append(canastas_1)
        canastas_2_punto.append(canastas_2)
        canastas_3_punto.append(canastas_3)
        # Anyadir el jugador
        jugadores_basket.append(nombre_jugador)
    else:
        print("Has introducido alguna canasta incorrecta")

# Salimos del bucle
for jugador in range(len(jugadores_basket)):
    anotacion_total_jugador = (canastas_1_punto[jugador] +
                            canastas_2_punto[jugador] * 2 + canastas_3_punto[jugador] *3)
    print(f"El jugador {jugadores_basket[jugador]} ha anotado {anotacion_total_jugador}")