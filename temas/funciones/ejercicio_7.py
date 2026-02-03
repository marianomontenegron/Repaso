import matplotlib.pyplot as plt
import numpy as np

def leerDatos():
  x = []
  y = []
  for i in range(5):
    dato_x = int(input("x= "))
    dato_y = int(input("y= "))
    x.append(dato_x)
    y.append(dato_y)

  return x,y

def calcular_a(x,y):
  a = (len(x)*np.sum(x*y)-np.sum(x)*np.sum(y))/(len(x)*np.sum(x**2)-np.sum(x)**2)
  return a

def calcular_b(x, y, a):
  b = 1 / len(x) * (np.sum(y) - a * np.sum(x))
  return b

def calcular_r2(x, y):
  r = (len(x)*np.sum(x*y)-np.sum(x)*np.sum(y)) / np.sqrt((len(x)*np.sum(x**2)-np.sum(x)**2) *(len(y)*np.sum(y**2)-np.sum(y)**2))
  return r

def graficar(x,y,a,b):
  x_grafica = np.arange(x.min(), x.max(),0.01)
  y_linea = a * x_grafica + b
  plt.scatter(x, y)
  plt.plot(x_grafica, y_linea)
  plt.show()


x,y = leerDatos()
x = np.array(x)
y = np.array(y)
a = calcular_a(x, y)
b = calcular_b(x, y, a)
r = calcular_r2(x, y)
print(f"a = {a}, b = {b}, r2 = {r**2}")
graficar(x,y,a,b)