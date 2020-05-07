def saludo(nombre : str) -> None:
    print("Hola",nombre)

def suma(a : int,b : int = 90) -> int:
    return a+b

saludo("Diego")
print(suma(1))