import random

# 1
for i in range(100+1):
    print(i)

# 2
n = int(input("ingrese un numero: "))
digitos = 0

for d in str(n):
    digitos += 1

print(f"{n} tiene {digitos} digitos")


# 3
n1 = int(input())
n2 = int(input())
r = 0

for n in range(n1+1, n2):
    r += n

# 4
ipt = int(input())
res = 0

while ipt != 0:
    res += ipt
    ipt = int(input())

print(res)

# 5
num_ipt = int(input())
respuesta = random.randrange(0, 9)
intentos = 0

while num_ipt != respuesta:
    num_ipt = int(input())
    intentos += 1

print(f"has acertado con {intentos} intentos")

# 6
for i in range(100+1):
    if i % 2 == 0: print(i)

# 7
num = int(input())
rs = 0

for i in range(0, num):
    rs += i

print(rs)

# 8
positivos = 0
negativos = 0
pares = 0
impares = 0

for i in range(100):
    nm = int(input())

    if nm > 0: positivos += 1
    elif nm < 0: negativos += 1
    
    if nm % 2 == 0: pares += 1
    else: impares += 1

print(f"numeros Positivos: {positivos}")
print(f"numeros Negativos: {negativos}")
print(f"numeros Pares: {pares}")
print(f"numeros Impares: {impares}")

# 9
res = 0
suma = 0
terminos = 0

for i in range(100):
    n_ipt = int(input())
    suma += n_ipt
    terminos += 1

print(f"la media es: {suma / terminos}")


# 10
numero_input = int(input("ingrese un numero: "))
numero_invertido = 0

while numero_input != 0:
    digito = numero_input % 10
    numero_invertido = numero_invertido * 10 + digito
    numero_input //= 10

print(str(numero_invertido))