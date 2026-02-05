class Ejercicio1():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.x = 0
    
    def leerDatos(self):
        self.a = int(input("Ingresa a: "))
        self.b = int(input("Ingresa b: "))
        self.c = int(input("Ingresa c: "))
        
    def realizarCalculo(self):
        self.x = ((self.b-(self.a**2))**(1/2))/self.c

    def mostrarresultado(self):
        print(f"x = {self.x}")
