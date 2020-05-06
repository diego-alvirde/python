def suma(a, b):
  """Función suma"""
  return a + b

def resta(a, b):
  """Función resta"""
  return a - b

opciones = {'a' : suma, 'b': resta}
print("Ingrese la opción deseada")

for opcion, funcion in opciones.items():
  mensaje = '{}) {}'.format(opcion, funcion.__doc__)
  print(mensaje)

opcion = input("Opción : ")

if opcion == "a":
  suma = suma(1,2)
  print(suma)
elif opcion == "b":
  resta = resta(35,2)
  print(resta)
else:
  print("Operación no valida")