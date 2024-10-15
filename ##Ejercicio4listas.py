##Ejercicio4listas.py

a= []

b= input("Escribe un nombre pon listo cuando termines:")
while b !="listo":
    a.append(b)
    b = input("Escribe un nombre pon listo cuando termines")

a= list(set(a))

c= max(set(a), key = a.count)
d= a.count(c)


print ("")

print("Resultado:")
for nombre in set(a):
    print(f"{nombre}: {a.count(nombre)} veces")
    
