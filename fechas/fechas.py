from datetime import date
from datetime import datetime
from datetime import timedelta

#Dia actual
today = date.today()

#Fecha actual
now = datetime.now()

print(today)
print(now)

#Atributos
#Date
#Date
print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))


#Datetime
print("El día actual es {}".format(now.day))
print("El mes actual es {}".format(now.month))
print("El año actual es {}".format(now.year))

print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))

#Fecha nueva
new_date = datetime(2019, 2, 28, 10, 15, 00, 00000)

print(new_date)

#Operaciones
#Sumar dos días a la fecha actual
now = datetime.now()
new_date = now + timedelta(days=2)
print(new_date)

#Comparación
if now < new_date:
    print("La fecha actual es menor que la nueva fecha")

#Formato de fechas
now = datetime.now()
format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
print(format)

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage

now = datetime.now()
print(current_date_format(now))