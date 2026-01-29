# Lista de compra de los ingredientes para hacer una
# tortilla de patatas
hay_patatas = False
hay_huevos = False
hay_aceite = False
hay_sal = False

# Preguntar al usuario
tienes_patatas = input("¿Tienes patatas? (s/n)")
if tienes_patatas == "s":
    hay_patatas = True
tienes_huevos = input("¿Tienes huevos? (s/n)")
if tienes_huevos == "s":
    hay_huevos = True
tienes_aceite = input("¿Tienes aceite? (s/n)")
if tienes_aceite == "s":
    hay_aceite = True
tienes_sal = input("¿Tienes sal? (s/n)")
if tienes_sal == "s":
    hay_sal = True

# Tengo que ir al super
if hay_patatas and hay_huevos and hay_aceite and hay_sal:
    print("Puedo hacer la tortilla de patatas")
else:
    print("Tengo que ir al super")

