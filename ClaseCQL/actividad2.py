# actividad2.py

# Mensaje de bienvenida
print("====================================")
print(" Calculadora de Índice IMC")
print("====================================")

# Solicitud de datos al usuario
nombre = input("Ingrese su nombre: ")
apellidos = input("Ingrese sus apellidos: ")
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Cálculo del IMC
imc = peso / (altura ** 2)

# Determinar clasificación del IMC
if imc < 18.5:
    clasificacion = "Bajo peso"
elif imc >= 18.5 and imc <= 24.9:
    clasificacion = "Peso normal"
elif imc >= 25 and imc <= 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

# Mostrar resultados
print("\n========== RESULTADOS ==========")
print("Nombre completo:", nombre, apellidos)
print("Edad:", edad, "años")
print("IMC calculado:", round(imc, 2))
print("Clasificación del IMC:", clasificacion)
print("================================")