import csv
import statistics
import datetime
from pdb import set_trace as bp
# long,lat,id_arbol,altura_tot,diametro,inclinacio,id_especie,nombre_com,nombre_cie,tipo_folla,espacio_ve,ubicacion,nombre_fam,nombre_gen,origen,coord_x,coord_y

nombre_archivo = 'arbolado-en-espacios-verdes.csv'

def writeFile(path, content):
    with open(path,"w+", encoding="utf-8") as file:
        file.write(content)

def groupBy(l, keyPredicate):
    groupBy = {}
    if isinstance(l, dict):
        for a in l:
            key = keyPredicate(a, l[a])
            if key not in groupBy:
                groupBy[key] = []
            groupBy[key].append(l[a])
    elif isinstance(l, list):
        for i in range(len(l)):
            key = keyPredicate(i, l[i])
            if key not in groupBy:
                groupBy[key] = []
            groupBy[key].append(l[i])
    return groupBy

def max(l, predicate):
    max = 0
    for e in l:
        localMax = predicate(l[e])
        if localMax > max:
            max = localMax
    return max

def findFirst(l, predicate):
    for e in l:
        if predicate(l[e]):
           return (e, l[e])
    return None

'''
Ejercicio 1:
Crear la función arboles_parque(nombre_archivo, nombre_parque) que dado el archivo 
nos genere una lista con un diccionario para cada árbol (identificado por su id) de ese parque (cada fila del csv) y 
los nombres de las columnas correspondientes como claves de un diccionario interno. 
'''
def arboles_parque(_nombre_archivo, nombre_parque):
    arboles = {}
    with open(_nombre_archivo, newline='', encoding="utf8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if nombre_parque is None:
                arboles[row["id_arbol"]] = row
            elif (row["espacio_ve"] == nombre_parque):
                arboles[row["id_arbol"]] = row
    return arboles


'''
Ejercicio 2:
Crear una función que aprovechando la anterior, nos indique el árbol más popular de ese parque: arbol_mas_popular(nombre_parque).
'''
def arbol_mas_popular(nombre_parque):
    arboles = arboles_parque(nombre_archivo,nombre_parque)
    arbolesPorNombre = groupBy(arboles, lambda k, v: v["nombre_com"])
    maxArbol = max(arbolesPorNombre, lambda a: len(a))
    popular = findFirst(arbolesPorNombre, lambda a: len(a) == maxArbol)
    return popular[0]


'''
Ejercicio 3:
Indicar los n árboles más altos de ese parque n_mas_altos(nombre_parque, n)
'''
def n_mas_altos(nombre_parque, n):
    arboles = arboles_parque(nombre_archivo,nombre_parque)
    data = [(key, arboles[key]["altura_tot"]) for key in arboles]
    data.sort(key=lambda e: e[1], reverse=True)
    r = [arboles[e[0]] for e in data[0: n]]
    return r


'''
Ejercicio 4:
Dado un parque y una especie, indicar la altura promedio de esa especie altura_promedio(nombre_parque, especie).
'''
def altura_promedio(nombre_parque, especie):
    arboles = arboles_parque(nombre_archivo,nombre_parque)
    arbolesFiltradoPorEspecie = [arboles[key] for key in arboles if arboles[key]["nombre_cie"] == especie]
    data = [int(a["altura_tot"]) for a in arbolesFiltradoPorEspecie]
    return statistics.mean(data)


'''
Ejercicio 5:
Probar el código creado y definir las funciones extra necesarias para decidir:

El/los parques con más cantidad de árboles.
El/los parques con los árboles más altos en promedio.
El/los parques con más variedad de especies.
La especie que más ejemplares tiene en la ciudad.
La razón entre especies exóticas y autóctonas.
'''

def pickMax(tally):
    if len(tally) == 0:
        return None
    tally.sort(key= lambda a: a[1], reverse=True)
    max = tally[0][1]
    return [e[0] for e in tally if e[1] >= max]


def getParquesMasForestados(arbolesPorParque):
    tally = [(key, len(arbolesPorParque[key])) for key in arbolesPorParque]
    return pickMax(tally)


def getParquesConArbolesMasAltosEnPromedio(arbolesPorParque):
    tally = [(key, statistics.mean([int(a["altura_tot"]) for a in arbolesPorParque[key]])) for key in arbolesPorParque]
    return pickMax(tally)


def getParquesConMasVariedadEspecies(arbolesPorParque):
    tally = [(key, len([b for b in groupBy([a["nombre_cie"] for a in arbolesPorParque[key]], lambda k, v: v) ])) for key in arbolesPorParque]
    return pickMax(tally)


def getEspecieMasPopular(arboles):
    arbolesPorEspecie = groupBy(arboles, lambda k, v: v["nombre_cie"])
    tally =[(key, len(arbolesPorEspecie[key])) for key in arbolesPorEspecie]
    return pickMax(tally)


def getRazonExoticosAutoctonos(arboles):
    arbolesPorOrigen = groupBy(arboles, lambda k, v: v["origen"])
    if len(arbolesPorOrigen) == 0:
        return None
    cant_exoticos = len(arbolesPorOrigen["Exótico"])
    cant_autoctonos = len(arbolesPorOrigen["Nativo/Autóctono"])
    if (cant_autoctonos == 0):
        raise "Cantidad autoctonos es 0."
    return  cant_exoticos / cant_autoctonos


def informe():
    arboles = arboles_parque(nombre_archivo,None)
    arbolesPorParque = groupBy(arboles, lambda k, v: v["espacio_ve"] )
    return {
        "parquesMasForestados": getParquesMasForestados(arbolesPorParque),
        "parquesConArbolesMasAltos": getParquesConArbolesMasAltosEnPromedio(arbolesPorParque),
        "parquesConMasVariedadEspecies": getParquesConMasVariedadEspecies(arbolesPorParque),
        "especieMasPopular": getEspecieMasPopular(arboles),
        "razonExoticosAutoctonos": getRazonExoticosAutoctonos(arboles)
    }

if __name__ == '__main__':
    nombre_parque = 'CENTENARIO'
    #arboles = arboles_parque(nombre_archivo, nombre_parque)
    popular = arbol_mas_popular(nombre_parque)
    print(f"El árbol más popular en el parque '{nombre_parque}' es {popular}.")
    n = 5
    arbolesMasAltos = n_mas_altos(nombre_parque, n)
    print(f"Los {n} árboles más altos en el parque '{nombre_parque}' son {' ,'.join(a["id_arbol"] for a in arbolesMasAltos)}.")
    especie = 'Washingtonia filifera'
    promedioAltura = altura_promedio(nombre_parque, especie)
    print(f"La altura promedio de los árboles de la especie '{especie}' en el parque '{nombre_parque}' es {round(promedioAltura,2)}.")
    _informe = informe()
    informe_str =f"# Reporte\n- {"El parque" if len(_informe["parquesMasForestados"]) <= 1 else "Los parques"} con más cantidad de árboles {"es" if len(_informe["parquesMasForestados"]) <= 1 else "son"}: **{" ".join(_informe["parquesMasForestados"])}**.\n- {"El parque" if len(_informe["parquesConArbolesMasAltos"]) <= 1 else "Los parques"} con los árboles más altos en promedio {"es" if len(_informe["parquesConArbolesMasAltos"]) <= 1 else "son"}: **{" ".join(_informe["parquesConArbolesMasAltos"])}**.\n- {"El" if len(_informe["parquesConMasVariedadEspecies"]) <= 1 else "Los"} parques con más variedad de especies {"es" if len(_informe["parquesConMasVariedadEspecies"]) <= 1 else "son"}: **{" ".join(_informe["parquesConMasVariedadEspecies"])}**.\n- {"La especie mas popular es" if len(_informe["especieMasPopular"]) <= 1 else "Las especies mas populares son"}: **{" ".join(_informe["especieMasPopular"])}**.\n- La razón entre especies exóticas y autóctonas: **{round(_informe["razonExoticosAutoctonos"],2)}**.\n\nCreado: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
    print(_informe)
    writeFile("informe_semana_04.md", informe_str)