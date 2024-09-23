#actividad 3
#parte 1
Ci = 100000
Interes = 0.02
ciclos = 10

Icompuesto= Ci *{1 + Interes}**ciclos
print(f"El valor final, con un capital de {Ci}, un interes de {Interes} con la cantidad de años {ciclos} es ")
print (Icompuesto)

#parte 2
Ci= int{input("Ingresar el valor inicial:")}
i = float (input("Indicar el valor de Interes (En decimales):"))
n = int (input("Indicar cantidad de ciclos/años:"))
Cf=Ci *(1+i)**n
print(f"El valor final, con un capital de {Ci}, un Interes de {i} con la cantidad de años {n} es")
print{Cf}

