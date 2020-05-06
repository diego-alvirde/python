class Circulo:
  pi = 3.14159265

  @classmethod
  def area(cls,radio):
    return cls.pi * radio**2

resultado = Circulo.area(10)
print(resultado)

class Rectangulo:
  def __init__(self,base,altura):
    self.base = base
    self.altura = altura

  def calcular_area(self):
    return self.base * self.altura

  @classmethod
  def cuadrado(cls, valor):
    return cls(valor,valor)

cuadrado = Rectangulo.cuadrado(5)
print(cuadrado.calcular_area())