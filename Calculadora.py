#Definimos funciones de la calculadora
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b

while True:
    operacion = input("Ingresa una operacion para calcular ('salir' para finalizar): ")
    if operacion.lower() == "salir":
        break
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    if operacion == "suma":
        Resultado=suma(a,b)
    if operacion == "resta":
        Resultado=resta(a,b)
    if operacion == "multiplicacion":
        Resultado=multiplicacion(a,b)
    if operacion == "division":
        Resultado=division(a,b)
    print(Resultado)


