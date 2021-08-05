#Conjuntos
#NO pueden haber duplicados

conjunto = set() #SE define la funcion set para definir que es un conjunto

conjunto = {1,2,3,"Victor",1.5}

print(conjunto)

#AGREGAR elementos al conjunto
#Los va a agregar en una posicion random
conjunto.add(4)
print(conjunto)

#ELIMINAR un elemento del conjunto
conjunto.discard(4)
print(conjunto)

#BUSCAR un elemento dentro del conjunto
print(f"El numero 1 esta en el conjunto?")
print(1 in conjunto)

#BUSCAR si un elemento NO esta en el conjunto
print("El numero 11 NO esta en el conjunto")
print(11 not in conjunto)

#LIMPIAR conjunto
#conjunto.clear()


'''
SI le vamos a poner datos desde el inicio
se puede omitir la funcion set()
'''

a = {1,2,3}
b = {3,4,5}

print("El conjunto a == b")
print(a == b)
print("Cuantos elementos tiene el conjunto a?")
print(len(a))

#UNION de conjuntos
c = a | b
print(c)

#INTERSECCION de dos conjuntos
d = a & b
print(d)

#DIFERENCIA (Lo que esta en a que no esta en b)
e = a - b
print(e)

#Lo que no esta en ambos
f = a ^ b
print(f)

#SUBCONJUNTO
g = {1,2,3,4,5,6}
print("Los elementos de a estan en g?")
print(a.issubset(g))

#SUPERCONJUNTO
print("Los elementos de g contienen los de a?")
print(g.issuperset(a))

#Los conjuntos NO comparten elementos en comun
print("Los conjuntos NO comparten elementos en comun")
print(a.isdisjoint(g))

#HACER un conjunto INMUTABLE
h = frozenset({1,2,3,4,5,6,7})
