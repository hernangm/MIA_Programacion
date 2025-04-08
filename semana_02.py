def invertir_lista(lista):
    l = []
    for i in range(len(lista),0,-1):
        l.append(lista[i-1])
    return l

if invertir_lista([1,2,3,4,5]) == [5,4,3,2,1]:
    print("Test 1 passed")

if invertir_lista(['Bogotá', 'Rosario', 'San Fernando', 'San Miguel']) == ['San Miguel', 'San Fernando', 'Rosario', 'Bogotá']:
    print("Test 2 passed")


'''
Ejercicio 2: Conjetura de Collatz
Escribir una función que compute la conjetura de Collatz para un número entero dado. La misma se puede enunciar como:

Empezamos con un número entero positivo,
Lo evaluamos, si el número es par entonces lo dividimos entre 2. Si es impar, entonces se multiplica por 3 y se le suma 1.
Al resultado lo volvemos a evaluar y nuevamente aplicamos las operaciones correspondientes hasta que obtengamos un 1.

Esto no se ha demostrdo pero funciona para todos los casos probados.

La función debe llamarse collatz.
'''
# def collatz(n):
#     cont = 0
#     if (n <= 0):
#         raise ValueError(f"El número n debe ser positivo ({n}).")
#     if (n == 1):
#         return 1, cont
#     if (n%2 == 0):
#         cont +=1
#         return collatz(n//2), cont
#     else:
#         cont +=1
#         return collatz(3*n+1), cont

def collatz(n):
    if (n <= 0):
        raise ValueError(f"El número n debe ser positivo ({n}).")
    if (n == 1):
        return 0
    if (n%2 == 0):
        return collatz(n//2) + 1
    else:
        return collatz(3*n+1) + 1
    
try:
    collatz(0)
except ValueError as e:
    print("Test Collatz 0 passed")

if collatz(1) == 0:
    print("Test Collatz 1 passed")
if collatz(2) == 1:
    print("Test Collatz 2 passed")
if collatz(3) == 7:
    print("Test Collatz 3 passed")

'''
    Ejercicio 3: Diccionarios
Dado un diccionario que dadas ciertas claves (que serán strings) tiene ciertas definiciones (lista de strings), dar dos funciones:

contar_definiciones(d) que dado un diccionario devuelve otro diccionario con las mismas claves y para cada una de ellas la cantidad de definiciones que tiene.
cantidad_de_claves_letra(d, l) que dado el diccionario d devuelve la cantidad de entradas (claves) que comienzan con la letra l.
'''
def contar_definiciones(d):
    d2 = {}
    for key in d:
        d2[key] = len(d[key])
    return d2

if contar_definiciones({"Pepe": [0,1],"Cacho":[0,1,2]}) == {"Pepe": 2,"Cacho":3}:
    print("Test contar_definiciones 1 passed")

def cantidad_de_claves_letra(d, l):
    cont = 0
    for key in d:
        if (key[0] == l):
            cont +=1
    return cont

if cantidad_de_claves_letra({"Pepe": [0,1],"Cacho":[0,1,2]}, "P") == 1:
    print("Test cantidad_de_claves_letra 1 passed")

'''
Ejercicio 4: Propagación
Vamos a modelar una fila con varios fósforos uno al lado del otro. Los fósforos pueden estar en tres estados: nuevos, prendidos fuego o ya gastados (carbonizados).
Representaremos esta situación con una lista L con un elemento por fósforo, que en cada posición tiene un 0 (nuevo), un 1 (encendido) o un -1 (carbonizado). 
El fuego se propaga inmediatamente de un fósforo encendido a cualquier fósforo nuevo que tenga a su lado. Los fósforos carbonizados no se encienden nuevamente.

Escribir una función llamada propagar que reciba una lista con 0’s, 1’s y -1’s y devuelva la lista en la que los 1’s se propagaron a sus vecinos con 0.

Por ejemplo:

>>> propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
[ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
>>> propagar([ 0, 0, 0, 1, 0, 0])
[ 1, 1, 1, 1, 1, 1]
'''

def propagar(lista):
    i = 0
    hasFlame = False
    while (i < len(lista)):
        if (lista[i] == 1):
            hasFlame = True
            j = i - 1
            while j >= 0:
                if (lista[j] == 0):
                    lista[j] = 1
                    j -= 1
                elif (lista[j] == -1 or lista[j] == 1):
                    break
        elif (lista[i] == 0):
            if hasFlame:
                lista[i] = 1
        elif (lista[i] == -1):
            hasFlame: False
        i += 1
    return lista

if __name__ == '__main__':
    p1 = propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
    if p1 == [ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]:
        print("Test propagar 1 passed")
    else:
        print(f"1:{p1}")

    p2 = propagar([ 0, 0, 0, 1, 0, 0])
    if p2 == [ 1, 1, 1, 1, 1, 1]:
        print("Test propagar 2 passed")
    else:
        print(f"1:{p2}")