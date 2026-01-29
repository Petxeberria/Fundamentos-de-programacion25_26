# Módulo para simular tiradas de dados de diferentes tipos
import random


# Funcion dado de 6 caras
def tirar_dado_6():
    return random.randint(1, 6)


# Funcion dado de 6 caras
def tirar_dado_12():
    return random.randint(1, 12)


# Funcion dado de n caras
def tirar_dado_n(caras):
    return random.randint(1, caras)

# Programa principal
if __name__ == "__main__":
    tirar_dado_6()
    resultado = tirar_dado_6()
    print(f"Resultado de un dado de 6 caras: {resultado}")
    resultado = tirar_dado_12()
    print(f"Resultado de un dado de 12 caras: {resultado}")
    resultado = tirar_dado_n(20)
    print(f"Resultado de un dado de 20 caras: {resultado}")