"""
Dado un diccionario, el cual almacena las calificaciones de un alumno, 
siendo las llaves los nombres de las materia y los valores las calificación, 
mostrar en pantalla el promedio del alumno.
"""
calificaciones = {"Español":6,"Matematicas":9,"Etica":7,"Ingles":9,"Historia":10}
print(calificaciones)
sumatoria = 0
lista = list(calificaciones.values())

for valor in lista:
  sumatoria = sumatoria + int(valor)

promedio = sumatoria / len(lista)
print("El promedio del alumno es:",promedio)

"""
A partir del diccionario del ejercicio anterior, mostrar en pantalla la materia con mejor promedio.
"""
lista_keys = list(calificaciones.items())
mayor = 0
materia_mayor = ""

for key, valor in lista_keys:
  if mayor < int(valor):
    mayor = int(valor)
    materia_mayor = key
  
print("La materia con mejor promedio es:",materia_mayor)

"""
Crear una lista la cual almacene 10 números positivos ingresados por el usuario, 
mostrar en pantalla: la suma de todos los números, el promedio, el número mayor y el número menor.
"""
lista = []
contador = 0
sumatoria = 0
while contador < 10:
  contador+=1
  valor = input("Ingrese un numero:\n")
  lista.append(int(valor))
  sumatoria = sumatoria + int(valor)

promedio = sumatoria / len(lista)

print(lista)
print("La sumatoria es:",sumatoria)
print("El promedio es", promedio)
print("El numero mayor es",max(lista))
print("El numero menor es",min(lista))

"""
Dado una lista de frases ingresadas por el usuario, mostrar en pantalla todas aquellas que sean palíndromo.
"""
lista_frases = ["hola","anita lava la tina","adios","como estas","oro"]

for valor in lista_frases:
  correcta = valor.replace(" ","")
  revez = valor[::-1].replace(" ","")
  if correcta == revez:
    print("La palabra",valor,"es un palíndromo")

"""
Mostrar en pantalla la cantidad de vocales que existe en una frase dada por el usuario.
Mostrar en pantalla la frecuencia de aparición de vocales en una frase dada por el usuario.
"""
buscar_vocales = "Hola como"
lista_vocales = ["a","e","i","o","u"]
contador = 0
ac,ec,ic,oc,uc = 0,0,0,0,0

for vocal in buscar_vocales:
  if vocal in lista_vocales:
    contador+=1
  if vocal == "a":
    ac+=1
  if vocal == "e":
    ec+=1
  if vocal == "i":
    ic+=1
  if vocal == "o":
    oc+=1
  if vocal == "u":
    uc+=1

print("La cantidad de vocales en la frase son",contador)
print("a",ac,"e",ec,"i",ic,"o",oc,"u",uc)

"""
Listar todos los números pares del 0 al 100
"""
for valor in range(0,101,2):
  print(valor)