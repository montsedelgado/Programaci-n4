##Ejercicio7 listas.py

def es_primo(a):
    if a <= 1:
        return False
    
    b = 2
    while b < a:
        if a % b == 0:
            break
        b+= 1
    return b == a


c = []
d = 2
while len(C) < 10:
    if es_primo(d):
       c.append(d)
    d += 1

print("Los primeros 10 numeros primos, ordemados de mayor a menor:")
print (c)

