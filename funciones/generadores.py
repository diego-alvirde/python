def tabla_multiplicar(numero, maximo=10):
  for posicion in range(1, maximo+1):
    yield numero * posicion, numero, posicion

for resultado, numero, posicion in tabla_multiplicar(7,20):
  print(numero,"*",posicion,"=",resultado)

def numeros_pares(maximo=10):
  for posicion in range(2, maximo+1,2):
    yield posicion

print(next(numeros_pares()))

for resultado in numeros_pares():
  print(resultado)
