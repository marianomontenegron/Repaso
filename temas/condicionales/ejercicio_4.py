def ejercicio4():

  a = int(input("Ingresa el valor de a:"))
  b = int(input("Ingresa el valor de b:"))
  c = int(input("Ingresa el valor de c:"))

  d = (b**2)-4*a*c

  if d>0:
      print('La figura es una Hipérbola')

  if d == 0 and a == 0 and c == 0:
    print('La figura es una Recta')
  else:
    print('La figura es una Parábola')

  if d < 0 and a == c:
    print('La figura es una Circunferencia')
  else:
    print('La figura es una Elipse')