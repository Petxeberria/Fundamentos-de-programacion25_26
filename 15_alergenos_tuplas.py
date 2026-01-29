# Tener una coleccions de alimentos alergenos
alergenos = ("gluten", "marisco", "huevos", "pescado", "cacahuetes",
             "soja", "leche", "queso")

# Preguntar al usuario un plato que le guste
plato_favorito = input("¿Cúal es tu plato favorito?")
ingredientes = []

# Ingredientes del plato favorito
while True:
    ingrediente = input(f"Dime un ingrediente del plato {plato_favorito} ('salir' para finalizar): ")
    if ingrediente.lower() == "salir":
        break
    ingredientes.append(ingrediente)

# Comprobar si alguno de los ingredientes es un alérgeno
alergenos_encontrados = []
for ingrediente in ingredientes:
    if ingrediente in alergenos:
        alergenos_encontrados.append(ingrediente)
        print(f"Cuidado {ingrediente} encontrado!!!!!!")

# Mostrar un listado
if len(alergenos_encontrados) > 0:
    print(f"En tu {plato_favorito} tienes los siguientes alergenos")
    for ingrediente in alergenos_encontrados:
        print(ingrediente)
else:
    print(f"En tu {plato_favorito} NO tienes alergenos")
