ejercicio bucles3.py

PIN_SECRETO = "1234"  # PIN correcto
intentos_restantes = 3  # Número de intentos permitidos

intentos_simulados = ["1111", "4321", "1234"]  # El tercer intento es el correcto

for pin_ingresado in intentos_simulados:
    print(f"Intentando con PIN: {pin_ingresado}")
    
    if pin_ingresado == PIN_SECRETO:
        print("Login correcto")
        break
    else:
        intentos_restantes -= 1
        if intentos_restantes > 0:
            print(f"PIN incorrecto. Te quedan {intentos_restantes} intentos.")
        else:
            print("Llamando al policía")
