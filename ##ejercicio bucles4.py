##ejercicio bucles4.py
Cateto1 = int(input("Escribe el valor de uno de tus catetos"))
Cateto2 = int("Escribe el valor de otro cateto")
Hipotenusa = (Cateto1**2+Cateto2**2)**(1/2)

while Cateto1 <= 0 or Cateto2 <= 0 :
    print(" Error, catetos deben ser mayor que cero")
    Cateto1 = int(input("Escribe el valor de uno de tus catetos"))
    Cateto2 = int("Escribe el valor de otro cateto")
    
if Cateto1 <=0:
    print("valores denegados, ingresa uno distinto 0")
else:
    print("Valores correctos")
    print(Hipotenusa)
    