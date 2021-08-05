# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("Hola mundo !!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("\U0001F62A")

nombre = input("Ingrese su nombre: ")
puntosp1 = 10

print(f"Bienvenido, {nombre} !!")
print(f"Este es el nivel 1 y tienes {puntosp1} puntos")
print(f"Cuantas horas tiene 1 dia en la tierra? ")
respuesta1 = input("Respuesta: ")
if respuesta1 == "24":
    print(f"CORRECTO, tienes {puntosp1} puntos")
else:
    puntosp1 -= 1
    print(f"INCORRECTO, pierdes 1 punto, tienes {puntosp1} puntos")