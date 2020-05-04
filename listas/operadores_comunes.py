lista = [8.17, 90, 1, 5, 44, 1.32,5]
print(lista)
#Ordenar lista asc
lista.sort()
#Imprimir lista ordenada asc
print(lista)
#Ordenar lista desc
lista.sort(reverse=True)
#Imprimir lista ordenada desc
print(lista)
#Opciones min, max
menor = min(lista)
print(menor)
mayor = max(lista)
print(mayor)
#Tamaño de la lista
longitud = len(lista)
print(longitud)
#Buscar valor en la lista
resultado = 8.17 in lista
print(resultado)
#Encontrar el indice de un elemento
indice = lista.index(8.17)
print(indice)
#Imprimir el numero de veces que aparece un numero
contador = lista.count(5)
print(contador)