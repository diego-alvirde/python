"""
lista = []

for valor in range(0,101):
  lista.append(valor)

print(lista)
"""

estructura = [valor for valor in range(0,101) 
if valor % 2 == 0
  if valor < 50 ]
print(estructura)

diccionario = { indice: valor for indice,valor in enumerate(estructura) }

print(diccionario)