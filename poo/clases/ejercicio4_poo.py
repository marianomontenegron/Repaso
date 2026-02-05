class Ejercicio4():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

    def leerdatos(self): 
        self.a = int(input("Ingresa el valor de a:"))
        self.b = int(input("Ingresa el valor de b:"))
        self.c = int(input("Ingresa el valor de c:"))
    
    def realizarCalculo(self):
        self.d = (self.b**2)-4*self.a*self.c

    def mostrarResultado(self):
        if self.d>0:
            print('La figura es una Hipérbola')

        if self.d == 0 and self.a == 0 and self.c == 0:
            print('La figura es una Recta')
        else:
            print('La figura es una Parábola')

        if self.d < 0 and self.a == self.c:
            print('La figura es una Circunferencia')
        else:
            print('La figura es una Elipse')