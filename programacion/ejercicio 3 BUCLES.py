##EJERCICIO 3 BUCLES
a=int(input("dame un numero entero positivo"))


for numero in range(a+1):
    if numero%2==0:
        continue
    else:
        print (numero, end= ",")
        
