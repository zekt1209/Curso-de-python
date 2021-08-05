#Ejercicio 3 - Pedir un caracter e identificar si es una vocal o no

caracter = input("Introduce un caracter: ").lower()
#letra = letra.lower()

if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
    print(f"El caracter {caracter} es una vocal")
else:
    print(f"El caracter {caracter} no es una vocal")

