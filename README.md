# Reto #8 😲
By Juan Esteban Molina Rey (eljuanessoy)

### 1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

+ Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```python
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
```

+ Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

```python
if __name__ == "__main__":
  c = float(input("Ingrese el valor del prestamo: "))
  i = float(input("Ingrese el interés al año: "))
  n = float(input("Ingrese la cantidad de meses: "))
  IC = (lambda c, i, n: c*((1+(i/12))**n))(c,i,n)

  print()
  print("El interés compuesto es del prestamo es " + str(IC))
```

+ El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

```python
if __name__ == "__main__":
  d = int(input("Ingrese el número de días: "))
  c = int(input("Ingrese la cantidad de personas contagiadas actualmente: "))
  TotaldeContagios = (lambda d, c: c*(2**d))(d,c)

  print()
  print(f"El total de personas contagiadas en NuncaLandia es de {TotaldeContagios} personas")
```
### 2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).



```python

```

### 3. Escriba una función recursiva para calcular la operación de la potencia.



```python

```

### 4. Utilice la siguiente plantilla de code para contar el tiempo:

```python
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```

Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.
**Importante:** Revisar este [hilo](https://stackoverflow.com/questions/8220801/how-to-use-timeit-module).


### 5. Crear cuenta en [stackoverflow](https://stackoverflow.com/) y adjuntar imagen en el repo

[![Stackoverflow-Perfil.png](https://i.postimg.cc/PxwdJPnb/Stackoverflow-Perfil.png)](https://postimg.cc/dkwbSQ1D)

### 6. Cosas de adultos....ir a [linkedin](https://www.linkedin.com/) y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.

+ Esta es mi cuenta de [linkedin](https://www.linkedin.com/in/juan-esteban-molina-rey-48b3bb297/).
