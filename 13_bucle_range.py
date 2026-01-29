# Range
lista_5_numeros = range(5)
print(lista_5_numeros)
print(list(lista_5_numeros))

# Imprimir los numeros
for numero in lista_5_numeros:
    print(numero)
print("-" * 15)

# Imprimir un rango con saltos
for numero in range(1,5,1):
    print(numero)
print("-" * 15)

# Imprimir numeros impares
for numero_impar in range(1,10,2):
    print(numero_impar)
print("-" * 15)

# Calcular la suma de los numeros del 2 al 100 primeros pares
suma = 0
for numero_par in range(2,101,2):
    suma = suma + numero_par
    print(f"El acumulado es {suma}, hasta el numero {numero_par}")
print(f"Resultado final {suma}") # Resultado final
