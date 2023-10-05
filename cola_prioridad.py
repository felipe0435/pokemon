class nodoCola(object):
    info, siguiente, prioridad = None, None, None


class Cola(object):
    def __init__(self):
        self.entrada, self.salida = None, None
        self.tamanio = 0


def arribo(cola, info, prioridad):
    nuevoNodo = nodoCola()
    nuevoNodo.info = info
    nuevoNodo.prioridad = prioridad
    if cola.salida is None:
        cola.salida = nuevoNodo
        cola.entrada = nuevoNodo
    else:
        actual = cola.salida
        siguiente = actual.siguiente
        while prioridad <= actual.prioridad:
            if prioridad > actual.prioridad:
                cola.salida.siguiente = actual
                cola.salida = nuevoNodo
                break
            elif siguiente == None:
                cola.entrada.siguiente = nuevoNodo
                cola.entrada = nuevoNodo
                break
            elif prioridad == actual.prioridad and prioridad > siguiente.prioridad:
                nuevoNodo.siguiente = siguiente
                actual.siguiente = nuevoNodo
                break
            else:
                if actual.siguiente != None:
                    actual = actual.siguiente
                    siguiente = actual.siguiente
                else:
                    actual = actual.siguiente
                    siguiente = None
    cola.tamanio += 1


def atencion(cola):
    info = cola.salida.info
    prio = cola.salida.prioridad
    cola.salida = cola.salida.siguiente
    if cola.salida is None:
        cola.entrada = None
    cola.tamanio -= 1
    return info, prio


def esVacia(cola):
    return cola.entrada is None


def imprimir(cola):
    colaAuxiliar = Cola()
    while not esVacia(cola):
        info, prioridad = atencion(cola)
        print(info)
        arribo(colaAuxiliar, info, prioridad)
    while not esVacia(colaAuxiliar):
        info, prioridad = atencion(colaAuxiliar)
        arribo(cola, info, prioridad)


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
        arribo(colaAuxiliar, info, cola.salidad.prioridad)
    while not esVacia(colaAuxiliar):
        info = atencion(colaAuxiliar)
        arribo(cola, info, colaAuxiliar.salidad.prioridad)
    if existe == True:
        return index
    else:
        return None
