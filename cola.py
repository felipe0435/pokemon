class nodoCola(object):
    info, siguiente = None, None


class Cola(object):
    def __init__(self):
        self.entrada, self.salida = None, None
        self.tamanio = 0


def arribo(cola, info):
    nuevoNodo = nodoCola()
    nuevoNodo.info = info
    if cola.salida is None:
        cola.salida = nuevoNodo
    else:
        cola.entrada.siguiente = nuevoNodo
    cola.entrada = nuevoNodo
    cola.tamanio += 1


def atencion(cola):
    info = cola.salida.info
    cola.salida = cola.salida.siguiente
    if cola.salida is None:
        cola.entrada = None
    cola.tamanio -= 1
    return info


def esVacia(cola):
    return cola.entrada is None


def imprimir(cola):
    colaAuxiliar = Cola()
    while not esVacia(cola):
        info = atencion(cola)
        print(info)
        arribo(colaAuxiliar, info)
    while not esVacia(colaAuxiliar):
        info = atencion(colaAuxiliar)
        arribo(cola, info)


def index_of(cola, parametro):
    colaAuxiliar = Cola()
    index = 0
    existe = False
    while not esVacia(cola):
        if cola.salida.info != parametro:
            index += 1
        else:
            existe = True
        info = atencion(cola)
        arribo(colaAuxiliar, info)
    while not esVacia(colaAuxiliar):
        info = atencion(colaAuxiliar)
        arribo(cola, info)
    if existe == True:
        return index
    else:
        return None
