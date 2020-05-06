class Animal:
  def comer(self):
    print("Comiendo")

  def dormir(self):
    print("Durmiendo")

  def comun(self):
    print("Método de la clase animal")

class Mascota:
  def fecha_adopcion(self,fecha):
    self.fecha_de_adopcion = fecha

  def comun(self):
    print("Método de la clase Mascota")

class Perro(Animal,Mascota):
  def __init__(self,nombre):
    self.nombre = nombre

  def ladrar(self):
    print("Ladrando")  

  def comun(self):
    print("Método de la clase Perro")

class Gato(Animal):
  def ronroneo(self):
    print("Ronroneo")

perro = Perro("perro")
perro.fecha_adopcion("Hoy")
print(perro.fecha_de_adopcion)
perro.comun()