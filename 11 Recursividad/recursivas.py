# 1
def fact(x):
    if x == 0: return 1
    elif x > 0: return x * fact(x - 1)

ipt = int(input("ingrese un numero para el factorial"))

print(fact(ipt))

# 2
inpt = int(input())
def fibonacci(x):
    if x == 0: return 0
    elif x == 1: return 1
    elif x < 0: return "La x no puede ser negativa."
    else: return fibonacci(x - 1) + fibonacci(x - 2)
    
# esto es para la secuencia
for i in range(inpt):
    print(fibonacci(i))


def expo(b, ex):
    if ex == 0:
        return 1
    elif b == 0: return 0
    elif ex < 0: return "El exponente no puede ser negativo para esta implementación recursiva simple."
    else: return b * expo(b, ex - 1)

# 3
while True:
    base = int(input("ingrese la base: "))
    exponente = int(input("ingrese el exponente: "))

    res = expo(base, exponente)
    print(res)
    break

# 4
def dec2bin(x):
    if x == 0: return "0"
    elif x == 1: return "1"
    elif x < 0: return "Error: Ingresa un número entero positivo."
    else: return dec2bin(x // 2) + str(x % 2)


# 5
def is_palindrome(w, start, end):
    if start >= end: return True
    if w[start] != w[end]: return False
    return is_palindrome(w, start + 1, end - 1)

# 6
def digit_sum(n):
    if not isinstance(n, int) or n < 0: return "Error: El número debe ser un entero positivo."
    if n < 10: return n
    return (n % 10) + digit_sum(n // 10)


# 7
def count_blocks(n):
    if n == 1: return 1
    else: return n + count_blocks(n - 1)

# 8
def digit_counter(n, d):
    if not (0 <= d <= 9):
        return "Error: El dígito a buscar debe estar entre 0 y 9."
    if n < 0:
        return "Error: El número debe ser un entero positivo."
    
    if n == 0:
        return 0
    ultimo_digito = n % 10

    contador_actual = 0
    if ultimo_digito == d:
        contador_actual = 1

    return digit_counter(n // 10, d) + contador_actual