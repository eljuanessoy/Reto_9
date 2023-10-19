# Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
def Carne(*args) -> float:
  TotalCarne = (6*n) + (7*m) + (k)
  return TotalCarne

if __name__ == "__main__":
  n = float(input("Ingrese la cantidad de gallinas: "))
  m = float(input("Ingrese la cantidad de gallos: "))
  k = float(input("Ingrese la cantidad de pollos: "))
  TotaldeCarne = Carne(n, m, k)
  
  print()
  print(f"El peso de la carne son {TotaldeCarne}kg")