# Ejercicio 1

lista = []
print("Ingresar 5 numeros a una lista")
lista.append(float(input("Ingresa el primer numero: ")))
lista.append(float(input("Ingresa el segundo numero: ")))
lista.append(float(input("Ingresa el tercer numero: ")))
lista.append(float(input("Ingresa el cuarto numero: ")))
lista.append(float(input("Ingresa el quinto numero: ")))

conjunto = set(lista)
lista = list(conjunto)
#Alternativa: lista = list(set(lista))

print(lista)

