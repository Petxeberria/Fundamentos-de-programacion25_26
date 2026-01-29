# Generara una lista de vacia de alumnos
alumnos = []

# Pregunta al profesor por el nombre
# calf en ciencias, humanidades, arte

while True:
    nombre = input("Introduce el nombre (o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    calf_ciencias = float(input(f"Introduce la calificación en ciencias de {nombre}: "))
    calf_humanidades = float(input(f"Introduce la calificación en humanidades de {nombre}: "))
    calf_arte = float(input(f"Introduce la calificación en artístico de {nombre}: "))
    alumno = {
        'nombre': nombre,
        'calf_ciencias': calf_ciencias,
        'calf_humanidades': calf_humanidades,
        'calf_arte': calf_arte,
    }

    alumnos.append(alumno)

# Mostrar la lista de alumnos y su expediente
print(f"---- LISTA DE {len(alumnos)} ALUMNOS ----")
for alumno in alumnos:
    print(f"Nombre: {alumno['nombre']}, Ciencias: {alumno['calf_ciencias']}, Humanidades: {alumno['calf_humanidades']}"
          f", Arte: {alumno['calf_arte']}")

