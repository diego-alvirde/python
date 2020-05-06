def decorador(function):
  def imprime():
    print("Se realizara una operación")
    function()
    print("Se termino la operacion")
  return imprime

@decorador
def suma():
  print(10+20)

@decorador
def resta():
  print(34-12)

suma()
print("\n")
resta()