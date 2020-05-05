def crear_mensaje(nombre):
  return "Hola {}, bienvenido al curso de python 3".format(nombre)

def suma(a,b,c):
  return a+b+c

def obtener_curso():
  return "Curso de Python", "Básico", 3.6

mensaje = crear_mensaje("Diego Armando Maradona")
print(mensaje)
print(suma(12,32,63))

curso, nivel, version = obtener_curso()
print(curso)
print(nivel)
print(version)