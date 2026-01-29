# Los datos de carla
nombre_carla = "Carla"
edad_carla = "21"
altura = 1.82
dorsal = 12

# Los datos de Lucia
nombre_lucia = "Lucia"

""" TRANSFORMACION CON LISTAS """
jugadora_carla = ["Carla", "21" , 1.82, 12]
jugadora_lucia = ["Lucia", "20" , 1.85, 23]

print(jugadora_carla)

# Acceder a un elemento
print(f"La edad de {jugadora_carla[0]} es {jugadora_carla[1]}")

# Posicion de campo
jugadora_carla.append("Pivot")
print(jugadora_carla)

# Eliminar la edad de Carla
# jugadora_carla.remove("21")
# print(jugadora_carla)

# Eliminar las edad
jugadora_lucia.pop(1)
jugadora_carla.pop(1)
print(jugadora_carla)

# Longitud de la lista
print(f"Tenemos {len(jugadora_carla)} datos de {jugadora_carla[0]}")