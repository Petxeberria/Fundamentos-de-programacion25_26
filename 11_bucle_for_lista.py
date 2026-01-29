# Lista de nombres
lista_nombres = ["Paco", "Pedro" , "Mauro", "Tere", "Jonathan"]
print(lista_nombres)

# Recorrer la lista con un for
for nombre in lista_nombres:
    print(nombre.upper())

# lista de numeros
lista_numeros = [1, 2, 7, 4, 5, 6, 76, 8, 9, 64]
for numero in lista_numeros:
    if numero > 10:
        print(f"{numero} es mayor a 10")
    print(numero)

# temperaturas de un sensor de un congelador
temperaturas_sensor = [-5, -6, -5, -8, 0, -4 ,-5]
for temperatura in temperaturas_sensor:
    if temperatura >=0:
        print(f"{temperatura} es mayor o igual a {0}")
        print("Existe un error en el congelador")
        break
    print(f"La temperatura es {temperatura}")
