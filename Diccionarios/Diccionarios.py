#Diccionarios

# Los elementos se guardan desordenados
# Tienen 2 elementos por posicion, CLAVE Y VALOR
# NO puede haber claves duplicadas

diccionario = {"azul":"blue", "rojo":"red", "verde":"green", "uno":1}
print(diccionario)

'''
BUSCAR un elemento especifico por clave
y se muestra el valor
'''
print("Como se dice azul en ingles? ")
print(diccionario["azul"])

#AGREGAR nuevos elementos al diccionario
diccionario["amarillo"] = "yellow"
print(diccionario)

#MODIFICAR
diccionario["azul"] = "BLUE"

#ELIMINAR
del(diccionario["verde"])

#EJEMPLO de diccionario
agenda = {"Victor":{"edad":20,"estatura":1.74},"Frisbit":[13,1.69], "Chino":[16,1.74]}
print(agenda)
print(agenda["Victor"])

lista = [1,2,3,4,5,"Victor"]



