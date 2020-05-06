class Usuario:
  def saluda(self, nombre):
    return "Función saludar" + nombre

objeto = Usuario()

#Saber de que tipo es un objeto
print(type(objeto))
print(objeto.saluda("Diego"))