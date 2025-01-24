"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    letras = {}
    with open('files/input/data.csv') as f:
        for line in f:
            letra, valor = line.strip().split('\t')[0], int(line.strip().split('\t')[1])
            if letra in letras:
                letras[letra].append(valor)
            else:
                letras[letra] = [valor]

    return sorted([(k, max(v), min(v)) for k, v in letras.items()])
