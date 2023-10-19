def Potencia_recursiva(n:int, x:float):
  if n == 0:
    return 1
  elif n == 1:
    return x
  else:
    return x * Potencia_recursiva(n-1, x)

if __name__ == "__main__":
  n = int(input("Ingrese un numero natural: "))
  x = float(input("Ingrese un numero real: "))
  Resultado = Potencia_recursiva(n, x)
  print(f"{x}^{n}={Resultado}")