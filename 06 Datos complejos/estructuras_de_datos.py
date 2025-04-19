import math

class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, e): 
        self.elementos.append(e)

    def descolar(self):
        self.elementos.pop(-1)


# 1
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000, 
    'Uva': 1450
}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# 2
precios_frutas["Banana"] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3
frutas = []

for k in precios_frutas:
    frutas.append(k)

# 4
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años")

# 5
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio**2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# 6

def balanceo(string):
    pila = []
    mapeo = {")": "(", "]": "[", "}": "{"}
    
    for c in string:
        
        if c in "([{":
            pila.append(c)

        elif c in "}])":
            if not pila or pila[-1] != mapeo[c]:
                return False
            pila.pop()

    return not pila

# 7 
class Banco:
    def __init__(self) -> None:
        self.cola_clientes = []
        self.turno_actual = 1
    
    def encolar(self):
        self.cola_clientes.append(self.turno_actual)
        self.turno_actual += 1

    def descolar(self):
        self.cola_clientes.pop(0)

    def mostrar_siguiente(self):
        if len(self.cola_clientes) > 1:
            print(f"El siguiente turno es el {self.cola_clientes[1]}")
        else:
            print("Ya no quedan mas clientes")


# 8
class Nodo:
    def __init__(self, dato, siguiente = None) -> None:
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self) -> None:
        #self.elementos = []
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente

# 9
def invertir(lista):
    anterior = None
    actual = lista.cabeza
    while actual != None:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente
        lista.cabeza = anterior