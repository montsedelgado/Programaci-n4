##Ejercicio3 listas.py
a= []

b= input("Escribe un nombre pon listo cuando termines:")
while b !="listo":
    a.append(b)
    b = input("Escribe un nombre pon listo cuando termines")

c= max(set(a), key = a.count)
d= a.count(c)

print(f"El nombre más comun es {c} con una frecuencia de {d} veces.")

