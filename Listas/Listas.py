#Listas

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

print(lista[0])

#Podemos recorrerlas de inicio a fin o de din a inicio con numeros negativos
#print(lista[0])
#print(lista[-1])

#Imprimir una sublista
# print(lista[0:3]) esto es n-1
# print(lista[:3]) desde el inicio, hasta el dato 2
# print(lista[:]) toda la lista completa
# print(lista[1:4]) ciertos datos solamente

#Determinar la cantidad de elementos en la lista
print("Cantidad de elementos en la lista: ")
print(len(lista))

#INSERTAR elementos en la lista
lista.append(6)

#INSERTAR en una posicion especifica
lista.insert(2,"Casimiercoles")

#INSERTAR varios elementos al final de la lista
lista.extend([3, 2, 1])

print(lista)

#BUSCAR elemento en la lista
print("Lunes" in lista)

#BUSCAR la posicion en la que esta un dato en la lista
print(lista.index("Lunes"))

#Saber cuantas veces aparece un valor
print(lista.count(3))

#ELIMINAR el ultimo elemento de la lista
lista.pop()

#ELIMINAR el valor de una posicion en espefico
lista.pop(1)

#ELIMINAR el valor que quieres eliminar
lista.remove("Lunes")

#ELIMINAR todos los elementos de la lista
lista.clear()

#INVERTIR la lista
lista.reverse()

#ORDENAR lista ascendentemente
lista.sort()

#ORDENAR lista descendentemente
lista.sort(reverse=True)

print(lista)

lista.append(5)
lista.append(6)
lista.append(7)
lista.insert(1,5.5)
lista.extend([8,9,10])
lista.remove(10)
print(lista)