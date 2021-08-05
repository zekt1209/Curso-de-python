#Condicionales combinados

edad = int(input("Digite su edad: "))

                        #opcion 2
if edad>0 and edad<100: #if: 0<edad<100:
    if edad>=18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
else:
    print("Datos incorrectos, vuelve a intentarlo")


