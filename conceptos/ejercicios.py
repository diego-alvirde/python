#Calcular area de un triangulo
base = int(input("Ingrese la base\n"))
altura = int(input("Ingrese la altura\n"))
area = base * altura
print(area)

#Convertir dolares a pesos
PESO = 24.37
dolares = float(input("Ingrese la cantidad de dolares\n"))
valor_pesos = dolares * PESO
print(valor_pesos)

#Convertir grados Centígrados a Fahrenheit
EQUIVALENTE = 32
MULTIPLICA = 9/5
grados = float(input("Ingrese los grados Centígrados\n"))
grados_fahrenheit = (grados * MULTIPLICA) + EQUIVALENTE
print(grados_fahrenheit)

#Promedio de alumno
MATERIAS = 5
espanol = float(input("Calificación Español\n"))
matematicas = float(input("Calificación Matemáticas\n"))
economia = float(input("Calificación Economía\n"))
programacion = float(input("Calificación Programación\n"))
ingles = float(input("Calificación Ingles\n"))
promedio = (espanol+matematicas+economia+programacion+ingles) / MATERIAS
print(promedio)
