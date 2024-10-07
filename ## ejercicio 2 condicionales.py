## ejercicio 7 condicionales
print ("Esta funcion calcula la hipotenusa de un triangulo rectangulo")
CatetoA = float(input("Dame el valor de A:"))
CatetoB= float(input("Dame el valor de B:"))

if CatetoA > 0 : #el valor debe ser mayor que 0
    if CatetoB > 0:
        print(f"El valor de la hipotenusa es : "{(CatetoA**2+CatetoB**2)**1/2}"
    else:
        print("B es menor o igual a cero, esto es un error")
else:
    print("A es menor o igual a cero, esto es un error")


              

