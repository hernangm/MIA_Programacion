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
def collatz(n):
    if (n <= 0):
        raise ValueError(f"El número n debe ser positivo ({n}).")
    if (n == 1):
        return 1
    if (n%2 == 0):
        return collatz(n//2)
    else:
        return collatz(3*n+1)


try:
    collatz(0)
except ValueError as e:
    print("Test Collatz 0 passed")

if collatz(1) == 1:
    print("Test Collatz 1 passed")
if collatz(2) == 1:
    print("Test Collatz 2 passed")
if collatz(3) == 1:
    print("Test Collatz 3 passed")