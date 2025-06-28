import csv
def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file, delimiter=";")
            datos = list(reader)
        key =""
        keys = list()
        val = ""
        vals = list()
        diccionario = dict()
        caso = 0
        for i in range(len(datos)):
            for j in range(len(datos[i])):
                for k in datos[i][j]:
                    if caso == 0:
                        if k != ":":
                            key += k
                        else:
                            keys.append(key)
                            key = ""
                            caso = 1
                    else:
                        val += k
                vals.append(val)
                val = ""
                caso = 0
        for i in range(len(keys)):

            if keys[i] in diccionario:
                diccionario[keys[i]].append(float(vals[i]))
            else:
                diccionario[keys[i]] = list()
                diccionario[keys[i]].append(float(vals[i]))
        return diccionario
    except FileNotFoundError as error:
        raise FileNotFoundError("no se pudo encontrar el archivo")


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    suma = 0
    divicion = 0
    for producto in data.keys():
        for valor in range(len(data[producto])):
            divicion +=1
            suma += data[producto][valor]
        print (f"{producto}: ventas totales ${suma:.2f}, promedio ${(suma/divicion):.2f}")
        divicion = 0
        suma = 0
