# Ejercicio 2

lista1 = ["Hola", "Celular", "Mundo", "Victor", "Chiquis", "Celular"]
lista2 = ["Hola", "Computadora", "Victor", "Jerarquia", "Baraja"]

a = set(lista1)
b = set(lista2)

union = list(a | b)
diferenciaA = list(a - b)
diferenciaB = list(b - a)
interseccion = list(a & b)

print(f"Union: {union}")
print(f"DiferenciaA: {diferenciaA}")
print(f"DiferenciaB: {diferenciaB}")
print(f"Interseccion: {interseccion}")






