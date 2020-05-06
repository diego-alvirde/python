class Usuario:

  def __init__(self, username='',correo='',nombre=''):
    self.username = username
    self.correo = correo
    self.nombre = nombre

  def saluda(self):
    return "Función saludar" + self.nombre

  def mostrar_username(self):
    print(self.username)

  def mostrar_nombre(self):
    print(self.nombre)

objeto = Usuario("Username","correo@mail.com","Nombre")

#Saber de que tipo es un objeto
print(type(objeto))
print(objeto.saluda())
objeto.mostrar_username()

objeto.mostrar_nombre()