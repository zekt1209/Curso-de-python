#Ejercicio 5 - Cajero automatico

saldo = float(1000.00)

print("\t*** Cajero automatico ***")

print("1- Ingresar dinero en la cuenta")
print("2- Retirar dinero de la cuenta")
print("3- Mostrar dinero disponible")
print("4- Salir")

opc = input("Seleccione una opcion: ")

print()

if opc == '1':
    deposito = float(input("Cuanto dinero desea depositar? "))
    saldo += deposito
    print(f"Tu saldo des de: {saldo}")
elif opc == '2':
    retiro = float(input("Cuanto dinero desea retirar? "))
    if retiro > saldo:
        print("No tiene esa cantidad de dinero")
    else:
        saldo -= retiro
        print(f"Tu saldo des de: {saldo}")
elif opc == '3':
    print(f"Su saldo es de: {saldo}")
elif opc == '4':
    print("Gracias por usar el programa :D")
    exit()
else:
    print("ERROR, Se equivoco de opcion de menu")


