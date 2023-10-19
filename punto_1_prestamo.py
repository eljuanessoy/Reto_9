# Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
if __name__ == "__main__":
  c = float(input("Ingrese el valor del prestamo: "))
  i = float(input("Ingrese el interés al año: "))
  n = float(input("Ingrese la cantidad de meses: "))
  IC = (lambda c, i, n: c*((1+(i/12))**n))(c,i,n)

  print()
  print("El interés compuesto es del prestamo es " + str(IC))