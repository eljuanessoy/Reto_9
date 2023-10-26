# Reto #9 😲
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

+ Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```python
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
```

+ Diseñe una función que lea 5 numeros reales y calcule el promedio. 

```python
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
```

+ Diseñe una función que lea 5 numeros reales y calcule la raíz cubica del menor numero. 

```python
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
```

### 3. Escriba una función recursiva para calcular la operación de la potencia.

+ Desarrollé una función que se invoca a sí misma para realizar la multiplicación. En cada iteración se le resta a la potencia una unidad hasta que se haya realizado la multiplicación un total de n veces. Y a partr de esto le pido al usuario que ingrese los valores de la base y el numero al cual sera elevado y se imprime el resultado.

```python
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

```python
import time

start_time = time.time()
def fibo_Recursivo(n : int )-> int:
  if n <=1:
    return 1
  else:
    return fibo_Recursivo(n-1)+fibo_Recursivo(n-2)  

if __name__ == "__main__":
  Serie = int(input("Ingresa el numero de la serie de Fibonacci: "))
  ResultadoFibo = fibo_Recursivo(Serie)
  print(f"La serie de Fibonacci hasta {Serie} es {ResultadoFibo}")
end_time = time.time()

timer = end_time - start_time
print(timer)

diftime = 2
if diftime < timer:
  print(f'Diferencia de tiempo significativa a partir de {Serie}')
```

### 5. Crear cuenta en [stackoverflow](https://stackoverflow.com/) y adjuntar imagen en el repo

[![Stackoverflow-Perfil.png](https://i.postimg.cc/PxwdJPnb/Stackoverflow-Perfil.png)](https://postimg.cc/dkwbSQ1D)

### 6. Cosas de adultos....ir a [linkedin](https://www.linkedin.com/) y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.

+ Esta es mi cuenta de [linkedin](https://www.linkedin.com/in/juan-esteban-molina-rey-48b3bb297/).
