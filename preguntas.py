"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    # Abro el archivo CSV en modo lectura
    with open('data.csv', 'r') as archivo_csv:
    # Creo un objeto lector CSV
        lineas = csv.reader(archivo_csv, delimiter='\t')
        # convierto cada linea en una lista
        lineas = list(lineas)

        suma_segunda_columna = 0
        # Itero sobre las filas de la lista
        for linea in lineas:
            suma_segunda_columna += int(linea[1])
        #devuelvo la suma
        return suma_segunda_columna

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
# Abro el archivo CSV en modo lectura
    with open('data.csv', 'r') as archivo_csv:
    # Creo un objeto lector CSV
        lineas = csv.reader(archivo_csv, delimiter='\t')
        # convierto cada linea en una lista
        lineas = list(lineas)

    lista1 = []
    for linea in lineas:
        lista1.append((linea[0], 1))
                
    diccionario = {}
    for key, value in lista1:
        if key not in diccionario.keys():
            diccionario[key]= []
        diccionario[key].append(value)

    new_sequence = []
    for key, value in diccionario.items():
        tupla = (key, sum(value))
        new_sequence.append(tupla)

    sorted_sequence = sorted ( new_sequence, key = lambda x: x[0])
    return sorted_sequence


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    # Abro el archivo CSV en modo lectura
    with open('data.csv', 'r') as archivo_csv:
    # Creo un objeto lector CSV
        lineas = csv.reader(archivo_csv, delimiter='\t')
        # convierto cada linea en una lista
        lineas = list(lineas)

    lista1 = []
    for linea in lineas:
        lista1.append((linea[0], int(linea[1])))
                
    diccionario = {}
    for key, value in lista1:
        if key not in diccionario.keys():
            diccionario[key]= []
        diccionario[key].append(value)

    new_sequence = []
    for key, value in diccionario.items():
        tupla = (key, sum(value))
        new_sequence.append(tupla)

    sorted_sequence = sorted ( new_sequence, key = lambda x: x[0])
    return sorted_sequence


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

     # Abro el archivo CSV en modo lectura
    with open('data.csv', 'r') as archivo_csv:
    # Creo un objeto lector CSV
        lineas = csv.reader(archivo_csv, delimiter='\t')
        # convierto cada linea en una lista
        lineas = list(lineas)

    lista1 = []
    for linea in lineas:
        fecha = linea[2].split("-")
        lista1.append((fecha[1], 1))
                
    diccionario = {}
    for key, value in lista1:
        if key not in diccionario.keys():
            diccionario[key]= []
        diccionario[key].append(value)

    new_sequence = []
    for key, value in diccionario.items():
        tupla = (key, sum(value))
        new_sequence.append(tupla)

    sorted_sequence = sorted ( new_sequence, key = lambda x: x[0])
    return sorted_sequence

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open('data.csv', 'r') as archivo_csv:
        lineas = csv.reader(archivo_csv, delimiter='\t')
        lineas = list(lineas)

    lista1 = []
    for linea in lineas:
        lista1.append((linea[0], int(linea[1])))
                
    diccionario = {}
    for key, value in lista1:
        if key not in diccionario.keys():
            diccionario[key]= []
        diccionario[key].append(value)
    
    new_sequence = []
    for key, value in diccionario.items():
        tupla = (key, max(value), min(value))
        new_sequence.append(tupla)
    
    sorted_sequence = sorted ( new_sequence, key = lambda x: x[0])
    
    return sorted_sequence


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    with open('data.csv', 'r') as archivo_csv:
        lineas = csv.reader(archivo_csv, delimiter='\t')
        lineas = list(lineas)

    lista1 = []
    for linea in lineas:
        datos = linea[4].split(",")
        for key in datos:
            key_valor= key.split(":")
            lista1.append((key_valor[0],key_valor[1]))
    
    diccionario = {}
    for par in lista1:
        if par[0] not in diccionario.keys():
            diccionario[par[0]]= []
        diccionario[par[0]].append(int(par[1]))
    
    new_sequence = []
    for key, value in diccionario.items():
        tupla = (key, min(value), max(value))
        new_sequence.append(tupla)
           
    sorted_sequence = sorted ( new_sequence, key = lambda x: x[0])
    
    return sorted_sequence


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    with open('data.csv', 'r') as archivo_csv:
        lineas = csv.reader(archivo_csv, delimiter='\t')
        lineas = list(lineas)

    lista1 = []
    for linea in lineas:
        lista1.append((linea[1], linea[0]))
                
    diccionario = {}
    for key, value in lista1:
        if key not in diccionario.keys():
            diccionario[key]= []
        diccionario[key].append(value)
        
    new_sequence = []
    for key, value in diccionario.items():
        tupla = (int(key), value)
        new_sequence.append(tupla)
    
    sorted_sequence = sorted ( new_sequence, key = lambda x: x[0])
    
    return sorted_sequence
    

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open('data.csv', 'r') as archivo_csv:
        lineas = csv.reader(archivo_csv, delimiter='\t')
        lineas = list(lineas)

    # Inicializar un diccionario para almacenar las letras únicas
    diccionario_letras = {}

    for linea in lineas:
        numero = int(linea[1])
        letra = linea[0]

        if numero not in diccionario_letras:
            diccionario_letras[numero] = []

        if letra not in diccionario_letras[numero]:
            diccionario_letras[numero].append(letra)
    
    for numero, letras in diccionario_letras.items():
        diccionario_letras[numero] = sorted(letras)

    # Ordenar el diccionario por las claves
    sorted_sequence = sorted(diccionario_letras.items(), key=lambda x: x[0])

    return sorted_sequence


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    with open('data.csv', 'r') as archivo_csv:
        lineas = csv.reader(archivo_csv, delimiter='\t')
        lineas = list(lineas)

    diccionario = {}

    for linea in lineas:
        datos = linea[4].split(",")
        for key_valor in datos:
            key, valor = key_valor.split(":")
            if key in diccionario:
                diccionario[key] += 1
            else:
                diccionario[key] = 1

    # Ordenar el diccionario por las claves
    diccionario_ordenado = {k: v for k, v in sorted(diccionario.items())}
    return diccionario_ordenado


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    with open('data.csv', 'r') as archivo_csv:
        lineas = csv.reader(archivo_csv, delimiter='\t')
        lineas = list(lineas)

    tuplas=[]
    for linea in lineas:
        letras = linea[3].split(",")
        dicc = linea[4].split(",")
        tuplas.append((linea[0],len(letras),len(dicc)))

    return tuplas

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    with open('data.csv', 'r') as archivo_csv:
        lineas = csv.reader(archivo_csv, delimiter='\t')
        lineas = list(lineas)
    
    lista1 = []
    for linea in lineas:
        for item in linea[3].split(","):
            lista1.append((item, int(linea[1])))

    diccionario = {}
    for key, value in lista1:
        if key not in diccionario.keys():
            diccionario[key] = 0
        diccionario[key] = diccionario[key] + value

    diccionario_ordenado = {k: v for k, v in sorted(diccionario.items())}

    return diccionario_ordenado

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    with open('data.csv', 'r') as archivo_csv:
        lineas = csv.reader(archivo_csv, delimiter='\t')
        lineas = list(lineas)

    tuplas=[]
    for linea in lineas:
        dicc = linea[4].split(",")
        sum=0
        for duo in dicc:
            valor = duo.split(":")
            sum += int(valor[1])
        tuplas.append((linea[0],sum))
    
    diccionario = {}
    for key, value in tuplas:
        if key not in diccionario.keys():
            diccionario[key] = 0
        diccionario[key] = diccionario[key] + value

    diccionario_ordenado = {k: v for k, v in sorted(diccionario.items())}
    return diccionario_ordenado
