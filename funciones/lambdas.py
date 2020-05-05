#Funciones lambda o funciones anonimas
def centigrados_a_farhenheit(grados):
  return grados*1.8+32

funcion_variable = centigrados_a_farhenheit
resultado = funcion_variable(32)
print(resultado)

mi_funcion = lambda grados=0 : grados*1.8+32

result = mi_funcion(32)
print(result)