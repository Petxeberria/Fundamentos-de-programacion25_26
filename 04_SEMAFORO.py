#Semaforo
verde =1
amarillo = 2
rojo=3

#Estado del semaforo
semaforo= rojo

#control de trafico
if semaforo == verde:
    print("Esta en verde")
    print("Puedes pasar")
elif semaforo == amarillo:
    print("Esta en amarillo")
    print("Puedes pasar")
elif semaforo == rojo:
    print("Esta en rojo")
    print("No puedes pasar")
else:
    print("El semaforo esta roto")

print("Continua despues del IF")

