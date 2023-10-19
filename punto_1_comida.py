# Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
if __name__ == "__main__":
  p = int(input("Ingrese la cantidad de panes: "))
  l = int(input("Ingrese la cantidad de bolsas de leche: "))
  h = int(input("Ingrese la cantidad de huevos: "))
  B = int(input("Ingrese el valor del billete con el que va a pagar: "))
  LasVueltas= (lambda a,b,c,d: d - ((300 * a) + (3300 * b) + (350 * c)))(p,l,h,B)

  print()
  if LasVueltas>0:
    print("El vendedor me debe dar $" + str(LasVueltas))
  if LasVueltas<0:
    print("Le debo al vendedor $" + str(LasVueltas))
  elif LasVueltas == 0:
    print("No debo ni me deben nada")