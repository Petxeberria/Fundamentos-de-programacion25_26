import random

# Lista de los palos
palos = ["Corazones","Diamantes","Treboles","Picas"]
# Variable que almacena los valores de la baraja
valores = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

# baraja
baraja = []

# Genero la baraja
for palo in palos:
    for valor in valores:
        # crear una carta
        carta = f"{valor} de {palo}"
        # añadir a la baraja
        baraja.append(carta)

# Barajar el mazo
random.shuffle(baraja)

# Mostrar la baraja desordenada
for carta in baraja:
    print(carta)