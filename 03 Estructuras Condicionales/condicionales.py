# Vladimir C. Sommer

from statistics import mode, median, mean
import random

# 1
edad = int(input("ingrese su edad: "))

if edad >= 18:
    print("Eres mayor de edad")

# 2
calificacion = int(input("ingrese su edad: "))

if calificacion >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3
num_ipt = int(input("ingrese un numero par"))

if num_ipt % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# 4
edad_ipt = int(input("ingrese su edad: "))

if edad_ipt < 12 and edad_ipt > 0:
    print("Niño/a")
elif edad_ipt >= 12 and edad_ipt < 18:
    print("Adolencente")
elif edad_ipt >= 18 and edad_ipt < 30:
    print("Adulto/a joven")
elif edad_ipt >= 30:
    print("Adulto/a joven")

# 5
password = input("ingrese una contraseña: ")

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and media > moda:
    print("Hay un sesgo a la derecha")
elif media < mediana and media < moda:
    print("Hay un sesgo a la izquierda")
else:
    print("No hay sesgo")

# 7
str_ipt = input("ingrese una palabra o frase: ").title()

if (str_ipt[-1] == "a" or 
    str_ipt[-1] == "i" or 
    str_ipt[-1] == "e" or
    str_ipt[-1] == "u" or
    str_ipt[-1] == "o"): str_ipt += "!"
else:
    pass

print(str_ipt)

# 8
mag = int(input("ingrese magnitud en la escala de Rchter: "))

if mag < 3: print("Muy leve")
elif mag >= 3 and mag < 4: print("Leve")
elif mag >= 4 and mag < 5: print("Moderado")
elif mag >= 5 and mag < 6: print("Fuerte")
elif mag >= 6 and mag < 7: print("Muy fuerte")
elif mag > 7: print("Extremo")

# 9
hemisferio = input("ingrese su hemisferio: ").upper()
mes = (input("ingrese el mes actual: ")).lower()
dia = int(input("ingrese su dia mensual actual"))

resultado = ""

if ((mes == "diciembre" and dia >= 21) or
    (mes == "enero" and (dia >= 1 and dia <= 31)) or
    (mes == "febrero" and (dia >= 1 and dia <= 28)) or
    (mes == "marzo" and (dia <= 20))
    ):

    resultado = "Verano" if hemisferio == "S" else "Invierno"

elif ((mes == "marzo" and dia >= 21) or
      (mes == "abril" and (dia >= 1 and dia <= 31)) or
      (mes == "mayo" and (dia >= 1 and dia <= 30)) or
      (mes == "junio" and (dia <= 20)) 
      ):
    
    resultado = "Otoño" if hemisferio == "S" else "Primavera"

elif ((mes == "junio" and dia >= 21) or
      (mes == "julio" and (dia >= 1 and dia <= 30)) or
      (mes == "agosto" and (dia >= 1 and dia <= 31)) or
      (mes == "septiembre" and (dia <= 20))
      ): 

    resultado = "Invierno" if hemisferio == "S" else "Verano"

elif ((mes == "septiembre" and dia >= 21) or
      (mes == "octubre" and (dia >= 1 and dia <= 31)) or
      (mes == "noviembre" and (dia >= 1 and dia <= 30)) or
      (mes == "diciembre" and (dia <= 20))
      ):
    resultado = "Primavera" if hemisferio == "S" else "Otoño"

print(f"Su estacion actual es {resultado}")