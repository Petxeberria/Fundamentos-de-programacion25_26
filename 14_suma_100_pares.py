# Suma de 100 pares
acumulado = 0
numeros_sumados = 0

for numero_par in range(2,1001,2):
    if numeros_sumados >= 100:
        break
    else:
        acumulado += numero_par # acumulado = aculmulado + ...
        numeros_sumados += 1
        print(f"Llevo {numeros_sumados} numeros pares")

print(f"La suma de los 100 primeros pares es {acumulado}")