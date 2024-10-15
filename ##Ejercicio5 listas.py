##Ejercicio5 listas.py

a= int(input("Introduce un número:"))

b= []


c = 1
for i in range (1, 21):
    c = a * (i)
    b.append(c)

print("Resultados de la multiplicacion de los primeros 20 numeros dados:")
for i, b in enumerate (b, start=1):
    print(f"Posición {i}: {b}")
    