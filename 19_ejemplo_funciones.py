# Funcion sin parametros
def saludar():
    print("Hola como estas")
def saludar_nombre(nombre="Marta"):
    print(f"Hola {nombre}. Como estas")

def saludar_nombre_tipo(nombre,tipo ="Hola"):
    print(f"{tipo} {nombre}. Como estas")


# Funcion que realice una suma
def suma(a, b):
    print(a + b)


def suma_return(a, b):
    print(a + b)
    return a + b

# Devolver multiples resultados
def cuadrados(a):
    result_cuadrados = []
    result_cuadrados.append(a*a)
    result_cuadrados.append(a*a*a*a)
    return result_cuadrados

# Uso de las funcions
saludar()
suma(3, 2)
resultado = suma_return(4, 20)

# Funciones con param con valor predeterminado
saludar_nombre()
saludar_nombre("Paco")

saludar_nombre_tipo(tipo="Señor",nombre="Paco")

# Devolviendo multiples resultados
print(cuadrados(2))

print("Fin de codigo")
