# Preguntar al usuario su nombre y DNI
nombres = []
identificador_personas = []

while True:
    nombre = input ("Introduce el nombre del persona (o 'salir'): ")
    if nombre.lower() == "salir":
        break
    identificador_persona = input("Introduce su identificacion: ")

    # Comprobacion de duplicidad
    #if nombre not in nombres:
    #    nombres.append(nombre)
    #    identificador_personas.append(identificador_persona)
    nombres.append(nombre)
    identificador_personas.append(identificador_persona)

# Imprimir por pantalla los registros
print(nombres)
print(identificador_personas)

# Imprimir nombres unicos usando SET
print(set(nombres))
print(set(identificador_personas))

# Numero de usuarios diferentes
print(f"Numero de usuarios registrados: {len(set(identificador_personas))}")