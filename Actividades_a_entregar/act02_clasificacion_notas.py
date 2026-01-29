# A partir de la actividad 2 "IMC y clasificación"
# Crear un pequeño script que clasifique las notas de un estudiante
# según la siguiente escala:
# 0-4.9: Suspenso
# 5.0-6.9: Aprobado
# 7.0-8.9: Notable
# 9.0-10: Sobresaliente


nota = 9.99 # nota del estudiante

# Calculo de notas


# Clasificar el resultado
if nota < 5.0:
    print("Suspenso")
#elif imc >= 18.5 and imc < 24.9:
elif 5.0 <= nota < 7.0:
    print("Aprobado")
elif 7.0 <= nota < 9.0:
    print("Notable")
elif nota <= 10:
    print("Sobresaliente")
else:
    print("Error")