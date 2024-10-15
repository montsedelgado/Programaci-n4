##Ejercicio2 listas.py
a = []
print ("Ingresa la lista de los nombres de las asignaturas del instituto BigBayData. com pon fin cuando ya no tengas  mas que agregar")
b = input("ingresa las asignaturas:")
c= input ("Agregar mas asignaturas ingresar si o no")
lista = [b]
while c == "si":
    d= input ("Ingresa la siguiente asignatura:")
    a.append(d)
    c = input("Agregar más asignaturass ingresar si o no")


for b in lista: 
    print ("")
    d = int(input(f"Ingresa el número de alumnos para ¨{b}:"))
    e = [float(input(f"Ingresa la puntuación del alumno {i + 1} para {b}:")) for i in range (d)]


    f= sum(e) / d
    g= sum(1 for punt in e if punt >= 6)

    curso_actual = [b, d, f, g]
    a.append(curso_actual)
print("")
print("Resultado de las evaluaciones este año:")
for curso in a:
    print(f"{curso[0]}: {curso[1]} alumnos, Nota media: {curso[2]}, Desaprobados: {curso[3]}")
    