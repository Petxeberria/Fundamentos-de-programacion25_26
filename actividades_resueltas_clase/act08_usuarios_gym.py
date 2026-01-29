# Preguntar  al usuario su nombre y DNI
# Almacenamos en listas diferentes
nombres = []
dnis = []

# Bucle de interación con el usuario
while True:
    nombre = input("Introduce tu nombre (o 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    dni = input("Introduce tu DNI: ")
    nombres.append(nombre)
    dnis.append(dni)

# Imprimir los usuarios y dnis
for i in range(len(nombres)):
    print(f"Nombre: {nombres[i]} con DNI: {dnis[i]}")

#i = 0
#for nombre in nombres:
#    print(f"Nombre: {nombre} con DNI:{dnis[i]}")
#    i += 1

# Calcular numero de usuarios diferentes en un dia
usuarios_diferentes = set (dnis)
print(f"Numero de usuarios diferentes: {len(usuarios_diferentes)}")