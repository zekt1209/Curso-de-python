#Condicionales - pida 3 numeros y diga cual es el mayor

num1 = int(input("Digita el primer numero: "))
num2 = int(input("Digita el segundo numero: "))
num3 = int(input("Digita el tercer numero: "))

if num1 >= num2 and num1 >= num3:
    print(f"El numero {num1} es el mayor")
elif num2 >= num1 and num2 >= num3:
    print(f"El numero {num2} es el mayor")
elif num3 >= num1 and num3 >= num2:
    print(f"El numero {num3} es el mayor")
elif num1 == num2 and num1 == num3:
    print(f"Los 3 numero son iguales y son el numero: {num1}")
