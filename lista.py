class nodoListaSimple(object):
    info, siguiente = None, None


class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar(lista, info):
    nodo = nodoListaSimple()
    nodo.info = info
    if lista.inicio is None:
        nodo.siguiente = lista.inicio
        lista.inicio = nodo
    else:
        actual = lista.inicio
        siguiente = lista.inicio.siguiente
        while siguiente is not None:
            actual = actual.siguiente
            siguiente = siguiente.siguiente
        nodo.siguiente = siguiente
        actual.siguiente = nodo
    lista.tamanio += 1


def imprimir(lista):
    actual = lista.inicio
    while actual is not None:
        print(actual.info)
        actual = actual.siguiente


def tamanio(lista):
    return lista.tamanio


def eliminar(lista, info):
    data = None
    # saber si es el primero de la lista
    if(lista.inicio.info == info):
        data = lista.inicio
        lista.inicio = lista.inicio.siguiente
        lista.tamanio -= 1
    else:      
        actual = lista.inicio
        siguiente = lista.inicio.siguiente
        while (siguiente is not None and info != siguiente.info):
            actual = actual.siguiente
            siguiente = siguiente.siguiente
        # saber si es el ultimo de la lista
        if(siguiente is not None):
            data = siguiente.info
            actual.siguiente = siguiente.siguiente
            lista.tamanio -= 1
    return data


def index_of(lista, info):
    actual = lista.inicio
    index = 0
    while actual.info is not info:
        index += 1
        actual = actual.siguiente
        if actual == None:
            return None
    return index


def index(lista, indice):
    actual = lista.inicio
    for _i in range(indice):
        actual = actual.siguiente
        if actual == None:
            return None
    return actual.info


def index_of_param(lista, param):
    actual = lista.inicio
    while actual.info is not param:
        pass
