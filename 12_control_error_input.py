# Pregunto al usuario si le gusta el zumo de naranja
respuesta = input("Te gusta el zumo de naranja [s|n]")

while respuesta.lower() != 's' and respuesta.lower() != 'n':
    respuesta = input("Te gusta el zumo de naranja [s|n]")

if respuesta.lower() == 's':
    print("Te gusta el zumo de naranja")

