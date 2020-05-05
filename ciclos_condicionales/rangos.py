for valor in range(1,101,2):
  print(valor)

lista = [1,2,3,4,5,6]

for valor in range( len(lista) ):
  print("indice:",valor, "valor:",lista[valor])

for indice , valor in enumerate(lista):
  print("indice:",indice, "valor:",valor)