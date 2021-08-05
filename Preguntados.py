#Programa personal preguntados

puntos = 10

print("Bienvenido a PREGUNTADOS")
print("\n\nLas reglas son simples, si respondes una pregunta mal, se te quita un punto, si respondes bien, te quedas como estas")

print("\n*** Primera pregunta ***\n")

pregunta1 = input("Cuantos dias tiene un anio? ")

if pregunta1 == "365":
    print(f"CORRECTO, tienes {puntos} puntos ...")
else:
    puntos -= 1
    print(f"INCORRECTO, Pierdes un punto, tienes: {puntos} puntos ...")

pregunta2 = input("Cuantas horas tiene un dia? ")
if pregunta2 == "24":
    print(f"CORRECTO, tienes {puntos} puntos ...")
else:
    puntos = puntos - 1
    print(f"INCORRECTO, tienes {puntos} puntos")