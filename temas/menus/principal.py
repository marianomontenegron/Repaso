from temas.basicos.ejercicio_1 import ejercicio_1
import temas.basicos.ejercicio_2 as fn
from temas.listas.ejercicio_3 import ejercicio_3
import temas.condicionales.ejercicio_4 as fd
from temas.ciclos.ejercicio_5 import ejercicio_5
import temas.graficas.ejercicio_6 as fc


def menu_principal():
    while True:
        print("Menu principal")
        print("1.- Ejercicio 1")
        print("2.- Ejercicio 2")
        print("3.- Ejercicio 3")
        print("4.- Ejercicio 4")
        print("5.- Ejercicio 5")
        print("6.- Ejercicio 6")
        print("7.- Ejercicio 7")
        print("8.- Salir")
        op = int(input("Elija opción: "))
        match(op):
            case 1:
                ejercicio_1()
            case 2:
                fn.ejercicio_2()
            case 3:
                ejercicio_3()
            case 4:
                fd.ejercicio4()
            case 5:
                ejercicio_5()
            case 6:
                fc.ejercicio_6()
            case 7:
                pass
            case 8:
                break
            case _:
                print("Opción no válida")