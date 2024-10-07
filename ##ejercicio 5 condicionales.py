##ejercicio 5 condicionales.py
seleccion = str (input{"Bienvenido a Bella Napoli. ¿Quiere unapizza vegetariana? SI/NO"})
if seleccion == "SI":
    ingrediente= str(input("Selecciono Vegetariano, elija su ingrediente; Tofu o Pimiento"))
    if ingrediente == "Pimiento":
        print("Usted eligio vegetariano con Pimiento")
    else:
        print("Usted eligio vegetariano con Tofi")
else:
    ingrediente= str(input("Selecciono No vegetariano, elija su ingrediente; Peperoni, Jamon o Salmon"))
    if ingrediente == "Peperoni": 
        print(f"Usted eligio No vegetariano con {ingrediente}")
    elif ingrediente == "Jamon": 
        print(f"Usted eligio No vegetariano con {ingrediente}")
    else:
        if ingrediente == "Salmon": 
        print(f"Usted eligio No vegetariano con {ingrediente}")
