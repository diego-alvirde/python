def suma(a,*args):
  total = 0
  for valor in args:
    total+=valor
  return total

def usuarios_autenticados(**kwargs):
  print(kwargs)

def combinacion(requerido,*args,**kwargs):
  print(requerido)
  print(args)
  print(kwargs)

total = suma(1,10,20,50)
print(total)
usuarios_autenticados(a=True,b=False)
combinacion(1,5,10,a=100,b=200)