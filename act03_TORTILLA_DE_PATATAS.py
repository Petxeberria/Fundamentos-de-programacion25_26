#Lista de tortilla de patatas
hay_patatas=False
hay_huevo=False
hay_aceite= False
hay_sal = False

#Pregutnas al usuario
tienes_patatas= input("Tienes patatas? (s/n)")
if tienes_patatas == "s":
    hay_patatas=True
tienes_huevos = input("Tienes huevos? (s/n)")
if tienes_huevos == "s":
    hay_huevo=True
tienes_aceite = input("Tienes aceites? (s/n)")
if tienes_aceite == "s":
    hay_aceite=True
tienes_sal = input("Tienes sal? (s/n)")
if tienes_sal == "s":
    hay_sal=True

#tengo que ir a comprar
if hay_patatas and hay_huevo and hay_aceite and hay_sal:
    print("Tienes todo")
else:
    print("Vete al super")
