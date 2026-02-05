import math
class Ejercicio2():
    def __init__(self):
        self.n = 0
    
    def leerdatos(self):
        self.n = int(input("Ingresa el valor de n:"))
    
    def realizarCalculos(self):
        self.x = math.sqrt(2*math.pi)*math.e**-self.n*self.n**(self.n+1/2)
    
    def mostrarResultado(self):
        print(f"n! es igual a: {self.x}")