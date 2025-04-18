import math

# 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4
def calcular_area_circulo(radio):
    return math.pi * (radio**2)

# 5
def segundos_a_horas(segundos):
    return segundos * (60**2)

# 6

def tabla_multiplicar(numero):
    for i in range(1, 10):
        print(f"{numero}x{i} : {numero*i}")

# 7
def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)

# 8

def calcular_imc(peso, altura):
    return peso / (altura**2)


# 9
def celsius_a_fahrenheit(celsius):
    return celsius * (9/5) + 32


# 10
def calcular_promedio(a, b, c):
    return (a+b+c) / 3