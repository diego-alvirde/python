class Gato:
  def __init__(self,nombre):
    self.nombre = nombre

  def __str__(self):
    return self.nombre

class Pato(object):
  def __init__(self,nombre):
    self.nombre = nombre

  def __str__(self):
    return self.nombre

gato = Gato("Don Gato")
gato.edad = 6
pato = Pato("Donald")

print(gato.__dict__,pato.__dict__)
