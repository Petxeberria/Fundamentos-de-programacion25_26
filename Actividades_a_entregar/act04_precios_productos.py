# A partir de la actividad 06 "puntuaciones basket"
# Crear un pequeño script que calcule el precio máximo y mínimo de
# una lista de productos que se compran en un supermercado y que se pedirán al usuario
# Al final del programa se calculará el total del gasto

# Listas
jugadores_basket = []

canastas_1_punto = []
canastas_2_punto = []
canastas_3_punto = []

# Bucle infinito con while
while True:
    nombre_jugador = input("Introduce tu nombre porfavor (o 'salir' para finalizar) ")
    if nombre_jugador.lower() == "salir":
        break

    # Preguntar por el numero de canastas
    canastas_1 = int(input(f" {nombre_jugador} Introduce el numero de manzanas que vas a comprar:  "))
    canastas_2 = int(input(f"{nombre_jugador} Introduce el numero de lechugas: "))
    canastas_3 = int(input(f"{nombre_jugador} Introduce el numero de tomates: "))

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
    print(f"{jugadores_basket[jugador]} tiene que pagar {anotacion_total_jugador} euros")