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