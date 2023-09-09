from datetime import datetime

#Constantes
diasDeLaSemana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
fecha = datetime.now()

#Entradas
edad = int(input("Por favor ingrese su edad: "))
edadProyectada = input("¿Cumpliste años en este año? Si o No ")

numeros = input("Por favor ingrese dos numeros: ")
diaSeleccionado = int(input("Por favor digita el número del 1 al 7 para mostrar el día de la semana donde 1 = Lunes y 7 = Domingo: "))

#Proceso 1
anoActual = fecha.year
anoNacimiento = anoActual - edad if edadProyectada == "si" or edadProyectada == "Si" else anoActual - (edad + 1)
edadAnoCurso = edad + 1 if edadProyectada == "si" or edadProyectada == "Si" else edad

#Proceso 2
if edad >= 16 and edad <= 70:
    habilitadoConductor = bool(input("Marque con x si se encuentra habilitado para conducir de lo contrario presione enter: "))
else:
    habilitadoConductor = False
    
puedeConducir = "Su edad es adecuada para conducir" if edad >= 16 else "Aun no tienes la edad para conducir"
permisoConducir = "Se encuentra habilitado para conducir" if habilitadoConductor == True else "No se encutra habilitado para conducir por ser adulto mayor o ser muy joven"
#Proceso 3
listaNumeros = numeros.split(' ') 
numeroMayor = listaNumeros[0] if listaNumeros[0] >= listaNumeros[1] else listaNumeros[1]

#Salida 1
print("El año de nacimiento es ", anoNacimiento ," y tu edad al finalizar el año es ", edadAnoCurso)
#Salida 2
print(puedeConducir, " y ", permisoConducir )
#Salida 3
print("El numero mayor digitado en su solicitud es: ",numeroMayor)
#Salida 4
print("El día de la semana seleccionado es: ", diasDeLaSemana[diaSeleccionado-1])
