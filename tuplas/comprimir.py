tupla = (1,2,3,4,5,6)
#uno, dos, tres, cuatro = tupla[0], tupla[1], tupla[2], tupla[3]
uno, dos, tres, *cuatro = tupla

print(uno)
print(dos)
print(tres)
print(cuatro)

tupla_uno = (1,2,3,4,5,6)
lista_uno = [10,20,30,40]

resultado = zip(tupla_uno, lista_uno)
resultado = tuple(resultado)
print(resultado)