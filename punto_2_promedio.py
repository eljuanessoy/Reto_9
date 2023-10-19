# Diseñe una función que lea 5 numeros reales y calcule el promedio.
def Promedio(*args) -> float:
    ResultadoPromedio = (a+b+c+d+e)/5
    return ResultadoPromedio

if __name__ == "__main__":
  a = float(input("Ingrese un número real: "))
  b = float(input("Ingrese un número real: "))
  c = float(input("Ingrese un número real: "))
  d = float(input("Ingrese un número real: "))
  e = float(input("Ingrese un número real: "))
  PromedioFinal = Promedio(a, b, c, d, e)

  print()
  print("El promedio es " +str(PromedioFinal))