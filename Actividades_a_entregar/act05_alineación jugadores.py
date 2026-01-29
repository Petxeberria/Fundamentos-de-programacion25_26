# A partir de la actividad 08 y 09 "usuarios registrados" y "expedientes de alumnos"
# Se pretende crear un script que trabaje tanto con listas como con diccionarios
# Para ello se va a preguntar al usuario por los nombres y al menos 2 características más de 
# cada jugador. Para tener una plantilla final de todos ellos con las características
# que se han ido pidiendo.

# Generara una lista de vacia de alumnos
jugadores = []
numero_jugador = 0

# Pregunta al profesor por el nombre
# calf en ciencias, humanidades, arte

while True:

    numero_jugador += 1

    nombre = input(f"Introduce el nombre del jugador {numero_jugador}ª (o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    edad = float(input(f"Introduce edad de {nombre}: "))
    pierna = input(f"Introdude pierna dominante de {nombre}: ")
    alumno = {
        'nombre': nombre,
        'edad': edad,
        'pierna': pierna,
    }

    jugadores.append(alumno)

# Mostrar la lista de alumnos y su expediente
print(f"---- LISTA DE {len(jugadores)} JUGADORES ----")
for alumno in jugadores:
    print(f"Nombre: {alumno['nombre']}, edad: {alumno['edad']}, pierna dominante: {alumno['pierna']}")


