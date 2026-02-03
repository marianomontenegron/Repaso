import math

def ejercicio_2():
    n = int(input("Ingresa el valor de n:"))

    x = math.sqrt(2*math.pi)*math.e**-n*n**(n+1/2)

    print(f"n! es igual a: {x}")