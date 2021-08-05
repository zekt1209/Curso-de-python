#Ejercicio 4 - Calculadora de 4 operaciones aritmeticas
#Suma, resta, multiplicacion y division

print(" *** CALCULADORA ***\n")

num1 = float(input("Digita el primer numero: "))
num2 = float(input("Digita el segundo numero: "))

print("Que operacion deseas realizar?\n")
print("S, s - Suma\nR, r - Resta")
print("P, p, M, m - Multiplicacion\nD, d - Division\n")
opc = input("Respuesta: ")
opc = opc.lower()

if opc == 's':
    resultado = num1 + num2
    print(f"El resultado de la Suma es: {resultado}")
elif opc == 'r':
    resultado = num1 - num2
    print(f"El resultado de la Resta es: {resultado}")
elif opc == 'p' or opc == 'm':
    resultado =  num1 * num2
    print(f"El resultado de la Multiplicacion es: {resultado:.2f}")
elif opc == 'd':
    resultado = num1 / num2
    print(f"El resultado de la Division es: {resultado:.2f}")
else:
    print("Se equivoco de operacion")


