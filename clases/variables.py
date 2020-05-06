class Circulo:
  pi = 3.14159265 #variable de clase
  def __init__(self, radio):
    self.radio = radio #variable de instancia

uno = Circulo(10)
dos = Circulo(20)

dos.radio = 100

print(uno.pi)
print(dos.pi)