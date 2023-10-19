# El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
if __name__ == "__main__":
  d = int(input("Ingrese el número de días: "))
  c = int(input("Ingrese la cantidad de personas contagiadas actualmente: "))
  TotaldeContagios = (lambda d, c: c*(2**d))(d,c)

  print()
  print(f"El total de personas contagiadas en NuncaLandia es de {TotaldeContagios} personas")