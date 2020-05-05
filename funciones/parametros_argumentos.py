def crear_usuario(nombre='', apellido='', edad=10):
  return {
    'nombre':nombre,
    'apellido':apellido,
    'nombre_completo': "{} {}".format(nombre,apellido),
    'edad':edad
  }

valores = crear_usuario(edad=28,nombre='Diego',apellido='Maradona')

print(valores["nombre"])
print(valores["apellido"])
print(valores["edad"])