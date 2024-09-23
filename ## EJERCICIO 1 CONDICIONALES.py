## EJERCICIO 1 CONDICIONALES
edad= int(input("Deecime tu edad y te digo si podes pasar:"))
compañado = str(input("Indica si estas acompañado o no con si o no:"))
if edad >= 18:
    print("podes pasar")
else:
    if compañado == "si":
        print("Podes pasar")
    else:
        print ("no podes pasar")
        