class Animal:
  def comer(self):
    print("Comiendo")

  def dormir(self):
    print("Durmiendo")

class Perro(Animal):
  def __init__(self,nombre):
    self.nombre = nombre

  def ladrar(self):
    print("Ladrando")  

class Gato(Animal):
  def ronroneo(self):
    print("Ronroneo")

perro = Perro("perro")
perro.ladrar()
perro.comer()
perro.dormir()
print("\n")
gato = Gato()
gato.ronroneo()
gato.comer()
gato.dormir()