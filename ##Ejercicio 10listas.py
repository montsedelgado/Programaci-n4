##Ejercicio 10listas.py

import random
a= input("Introduce los correos electronicos de los solicitantes por comas: ")
b= a.spilt (",")

def seleccionar_ayudas (b, n):
    return random.sample(b,n)


correos_seleccionados = seleccionar_ayudas (b, 3)
print( "correos seleccionados para ofrecer ayuda:" , correos_seleccionados)
