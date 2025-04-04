'''
El objetivo de esta actividad es modelar y hacer un programa en Python que responda la pregunta:
¿cuántas figuritas hay que comprar para completar el álbum del Mundial?

Datos:
Álbum con 860 figuritas.
Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
Cada paquete trae cinco figuritas.
'''
import random
import statistics
import math

def printResult(repeticiones, estimacion, figus_total, unidad):
    print(f"{repeticiones} repeticiones de un experimento predicen que es necesario comprar {math.ceil(estimacion)} ({round(estimacion,2)}) {unidad} para poder llenar un album de {figus_total} figuritas.")

'''
Ejercicio 1: Crear}
Implementá la función crear_album(figus_total) que devuelve un álbum (vector) vacío con figus_total espacios para pegar figuritas.
'''
def crear_album(figus_total):
    return [0 for x in range(figus_total)]

'''
Ejercicio 2: Incompleto
Implementá la función album_incompleto(A) que recibe un vector y devuelve
True si el álbum A no está completo y 
False si está completo.
'''
def album_incompleto(album):
    return 0 in album

'''
Ejercicio 3: Comprar
Implementá una función comprar_figu(figus_total) que reciba el número total de figuritas que tiene el álbum (dado por el parámetro figus_total) y devuelva un número entero aleatorio que representa la figurita que nos tocó.
'''
def comprar_figu(figus_total):
    return random.randint(0, figus_total - 1)

'''
Ejercicio 4: Cantidad de compras
Implementá la función cuantas_figus(figus_total) que, dado el tamaño del álbum (figus_total),
genere un álbum nuevo, simule su llenado y devuelva la cantidad de figuritas que se debieron comprar para completarlo.
'''
def cuantas_figus(figus_total):
    figus_compradas = 0
    album = crear_album(figus_total)
    _album_incompleto = album_incompleto(album)
    while _album_incompleto:
        nueva_figu = comprar_figu(figus_total)
        album[nueva_figu] += 1
        figus_compradas += 1
        _album_incompleto = album_incompleto(album)
    return figus_compradas

'''
Ejercicio 6:
Escribí una función llamada experimento_figus(n_repeticiones, figus_total) 
que simule el llenado de n_repeticiones álbums de figus_total figuritas y 
devuelva el número estimado de figuritas que hay que comprar, en promedio, 
para completar el álbum.
Para esto, una posibilidad es que la función experimento_figus() llame a la
función cuantas_figus() tantas veces como lo indica el parámetro n_repeticiones
y guarde los resultados parciales en una lista, a partir de la cual luego 
realice el promedio.

¿Cuál es el resultado para 100 repeticiones en un álbum de 860 figuritas?
'''

def experimento_figus(n_repeticiones, figus_total):
    resultados = []
    for i in range(0, n_repeticiones):
        r = cuantas_figus(figus_total)
        resultados.append(r)
    estimacion = statistics.mean(resultados)
    return estimacion

'''
Ejercicio 8:
Implementá una función comprar_paquete(figus_total, figus_paquete) que, dado el tamaño del álbum (figus_total)
y la cantidad de figuritas por paquete (figus_paquete), genere un paquete (lista) de figuritas al azar.
'''
def comprar_paquete(figus_total, figus_paquete):
    return [comprar_figu(figus_total) for x in range(figus_paquete)]


'''
Ejercicio 9:
Implementá una función cuantos_paquetes(figus_total, figus_paquete) que dado el tamaño del álbum y 
la cantidad de figus por paquete, genere un álbum nuevo, simule su llenado y devuelva cuántos paquetes
se debieron comprar para completarlo.
'''
def cuantos_paquetes(figus_total, figus_paquete):
    cant_paquetes = 0
    album = crear_album(figus_total);
    _album_incompleto = album_incompleto(album)
    while _album_incompleto:
        paquete = comprar_paquete(figus_total, figus_paquete)
        for f in paquete:
            album[f] +=1
        cant_paquetes += 1
        _album_incompleto = album_incompleto(album)
    return cant_paquetes


def experimento_paquetes(n_repeticiones, figus_total, figus_paquete):
    resultados = []
    for i in range(0, n_repeticiones):
        r = cuantos_paquetes(figus_total,figus_paquete)
        resultados.append(r)
    estimacion = statistics.mean(resultados)
    return estimacion



if __name__ == '__main__':
    '''
    Ejercicio 5:
    Ejecutá n_repeticiones = 1000 veces la función anterior utilizando figus_total = 6 y 
    guardá en una lista los resultados obtenidos en cada repetición. Con los resultados obtenidos
    estimá cuántas figuritas hay que comprar, en promedio, para completar el álbum de seis figuritas.
    Ayuda: la media o promedio se calcula como la suma de todos los elementos divididos la cantidad.
    '''

    n_repeticiones = 1000
    figus_total = 6
    resultados = []
    for i in range(0, n_repeticiones):
        r = cuantas_figus(figus_total)
        resultados.append(r)
    estimacion = statistics.mean(resultados)
    printResult(n_repeticiones, estimacion, figus_total, "figuritas")

    '''
    Ejercicio 7:
    Simulá la generación de un paquete con cinco figuritas, sabiendo que el álbum es de 860. 
    Tené en cuenta que, como en la vida real, puede haber figuritas repetidas en un paquete.
    '''

    n_repeticiones = 100
    figus_total = 860
    estimacion = experimento_figus(n_repeticiones, figus_total)
    printResult(n_repeticiones,estimacion,figus_total, "figuritas")

    '''
    Ejercicio 10:
    Calculá n_repeticiones = 100 veces la función cuantos_paquetes, utilizando figus_total = 860, 
    figus_paquete = 5. Guarda los resultados obtenidos en una lista y calculá su promedio. Si los 
    recursos de la computadora lo permiten, hacelo con 1000 repeticiones.
    '''
    n_repeticiones = 1000
    figus_total = 860
    figus_paquete = 5
    estimacion = experimento_paquetes(n_repeticiones, figus_total, figus_paquete)
    printResult(n_repeticiones,estimacion,figus_total, "paquetes")