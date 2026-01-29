"""
Lista de la compra para hacer una tortilla de patatas
"""

# Lista vacia de la compra
lista_compra = []

# ¿Que nos falta?
ingrediente = input("¿Tienes patatas [s|n]?")
if ingrediente.lower() == "n":
    lista_compra.append("patatas")
ingrediente = input("¿Tienes huevos [s|n]?")
if ingrediente.lower() == "n":
    lista_compra.append("huevos")

if input("¿Tienes sal [s|n]?").lower() == "n":
    lista_compra.append("sal")
if input("¿Tienes aceite [s|n]?").lower() == "n":
    lista_compra.append("aceite")

# ¿Tengo que ir al supermecado?
if len(lista_compra) == 0:
    print("No tengo que ir al supermercado")
else:
    print("Si tengo que ir al supermercado")
    print(lista_compra)

# FORMA DOS DE RESOLUCION
if len(lista_compra) >= 1:
    print("Si tengo que ir al supermercado")
    print(lista_compra)
else:
    print("No tengo que ir al supermercado")