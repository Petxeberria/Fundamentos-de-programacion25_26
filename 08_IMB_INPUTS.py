"""
Programa calculo imc preguntas peso y altura
"""

#Pedir peso y altura
peso= float(input(
    "Introduce tu peso en kg: "
))
altura = float(input("Introduce tu altura en metros: "))

#Calculo de IMC
#imc = peso / (altura * altura)
imc = peso / (altura **2)
print (imc)
if imc < 18.5:
    print("Deficit de peso")
elif 18.5<=imc and imc < 24.9:
    print("Peso normal")
elif 24.9 <= imc and imc < 29.9:
    print("Sobrepeso")
elif 29.9 <= imc:
    print("Obesidad")
else:
    print("Error")