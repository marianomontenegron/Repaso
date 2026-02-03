import math

def ejercicio_5():

  x = float(input("ingresa la x: "))
  tol = float(input("ingresa la tolerancia: "))

  tan = math.atan(x)
  print(f"valor real = {tan}")
  k = 0
  serie = 0
  while True:
    serie += (-1)**k * (x**(2*k+1))/(2*k+1)
    k += 1
    error = math.fabs((tan - serie)/tan)*100
    if error < tol:
      break

  print(f"Error = {error}")
  print(f"Aproximación = {serie}")