# Diseñe una función que lea 5 numeros reales y calcule la raíz cubica del menor numero.
def RaizCubica(*args) -> float:
    ListaE = [*args]
    menor1 = min(ListaE)
    ResultadoRaizCubica = menor1**(1/3)
    return ResultadoRaizCubica

if __name__ == "__main__":
  a = float(input("Ingrese un número real: "))
  b = float(input("Ingrese un número real: "))
  c = float(input("Ingrese un número real: "))
  d = float(input("Ingrese un número real: "))
  e = float(input("Ingrese un número real: "))
  RaizCubicaFinal = RaizCubica(a, b, c, d, e)

  print("La raíz cúbica del menor número es: " +str(RaizCubicaFinal))