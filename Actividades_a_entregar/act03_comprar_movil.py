# A partir de la actividad 03 "tortilla de patatas"
# Crear un pequeño script que le devuelva al ususario qué móvil
# puede comprarse en función del dinero
# el sistema operativo que prefiere (iOS o Android)
# y si la cámara es importante para él o no.

# Script para recomendar móvil según preferencias del usuario

# Pedimos datos al usuario
cantidad_dinero = input("¿Cuál es tu presupuesto para el móvil (€)? ")
sistema_operativo = input("¿Qué sistema operativo prefieres? (iOS / Android): ")
camara = input("¿La cámara es importante para ti? (s/n): ")

# -----------------------------
# Normalizamos los datos
# -----------------------------

# Convertimos dinero a número (con seguridad)
if cantidad_dinero.isdigit():
    presupuesto = int(cantidad_dinero)
else:
    print("Has introducido un presupuesto inválido.")
    exit()

# Pasamos sistema a minúsculas
sistema_operativo = sistema_operativo.lower()

# Convertimos cámara a True / False
if camara.lower() == "s":
    camara = True
else:
    camara = False

# -----------------------------
# Lógica de recomendación
# -----------------------------

print("\nRecomendación:")

if sistema_operativo == "ios":

    if presupuesto < 500:
        if camara:
            print("Te recomendamos un iPhone 13 o iPhone 14 reacondicionado.")
        else:
            print("Te recomendamos un iPhone SE.")

    elif presupuesto < 900:
        if camara:
            print("Te recomendamos un iPhone 14 o iPhone 15.")
        else:
            print("Te recomendamos un iPhone 13.")

    else:
        print("Te recomendamos un iPhone 15 Pro o superior.")


elif sistema_operativo == "android":

    if presupuesto < 300:
        if camara:
            print("Te recomendamos un Samsung Galaxy A15 o Xiaomi Redmi Note.")
        else:
            print("Te recomendamos un Xiaomi básico.")

    elif presupuesto < 600:
        if camara:
            print("Te recomendamos un Samsung Galaxy A54 o Pixel 6a.")
        else:
            print("Te recomendamos un Samsung Galaxy A34.")

    else:
        print("Te recomendamos un Samsung Galaxy S23 / Pixel 8.")


else:
    print("Sistema operativo no reconocido. Elige iOS o Android.")
