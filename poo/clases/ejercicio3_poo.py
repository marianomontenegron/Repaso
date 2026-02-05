class Ejercicio3():
    def __init__(self):
        self.lista = []
    
    def leerDatos(self):
        self.lista = [1,2,3,[9,8,7,[6,5,4]]]

    def mostrarResultado(self):
        print(self.lista[1])
        print(self.lista[3][1])
        print(self.lista[3][3][2])