lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"
#Separador por default es el espacio
separador = "; "
resultado = lenguajes.split(separador)
nuevo_string = " ".join(resultado)
texto = """Texto
con saltos
de
linea
"""
resultado_salto_de_linea = texto.splitlines()

print(resultado)
print(nuevo_string)
print(resultado_salto_de_linea)