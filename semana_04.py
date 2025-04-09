import csv
# long,lat,id_arbol,altura_tot,diametro,inclinacio,id_especie,nombre_com,nombre_cie,tipo_folla,espacio_ve,ubicacion,nombre_fam,nombre_gen,origen,coord_x,coord_y

nombre_archivo = 'arbolado-en-espacios-verdes.csv'

def groupBy(l, keyPredicate):
    groupBy = {}
    for a in l:
        key = keyPredicate(a, l[a])
        if key not in groupBy:
            groupBy[key] = []
        groupBy[key].append(l[a])
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

def map(l, transform):
    output=[]
    for k in l:
        output.append(transform(k, l[k]))
    return output

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
            if (row["espacio_ve"] == nombre_parque):
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
    data = map(arboles, lambda k, v: (k, v["altura_tot"]))
    data.sort(key=lambda e: e[1], reverse=True)
    r = [arboles[e[0]] for e in data[0: n]]
    return r


if __name__ == '__main__':
    nombre_parque = 'CENTENARIO'
    #arboles = arboles_parque(nombre_archivo, nombre_parque)
    popular = arbol_mas_popular(nombre_parque)
    print(f"El arbol mas popular es {popular}")
    arbolesMasAltos = n_mas_altos(nombre_parque, 5)
    print(f"Los arboles mas altos son {' ,'.join(a["id_arbol"] for a in arbolesMasAltos)}")