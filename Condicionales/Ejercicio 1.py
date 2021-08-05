#Condicionales - Pide 2 numeros impares y dice cual de ellos es par o si ambos lo son

numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo numero: "))

if numero1%2 == 0 or numero2%2 == 0:
    if numero1%2 == 0 and numero2%2 == 0:
        print(f"Ambos numero SON PARES, y son: {numero1} y {numero2}")
    elif numero1%2 == 0:
        print("El primer numero es par")
    elif numero2%2 == 0:
        print("El segundo numero es par")
else:
    print(f"No hay ningun numero par")

