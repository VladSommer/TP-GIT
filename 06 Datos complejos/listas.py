# 1
lista_numeros = [x for x in range(1, 100+1) if x % 4 == 0]

# 2
lenguajes = ["Python", "Java", "C#", "C++", "Rust"]

print(lenguajes[-2])


# 3
lista_vacia = []


# 4
animales = ["perro", "gato", "conejo", "pez"]

animales[2] = "loro"
animales[-1] = "oso"

# 5
# Definir la lista
numeros = [8, 15, 3, 22, 7]

# Eliminar el elemento mas grande
numeros.remove(max(numeros))

# Imprimir la lista
print(numeros)

# 6
lista_num = [x for x in range(10, 30+1, 5)]

# 7
autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "toyota"
autos[2] = "mitsubishi"

# 8

dobles = []

for i in range(5, 15+1, 5): dobles.append(i*2)

print(dobles)

# 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

#10
lista_anidada = [0, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)