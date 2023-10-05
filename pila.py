class nodoPila(object):
    info, siguiente = None, None


class Pila(object):
    def __init__(self):
        self.cima = None
        self.tamanio = 0


def apilar(pila, info):
    nuevoNodo = nodoPila()
    nuevoNodo.info = info
    nuevoNodo.siguiente = pila.cima
    pila.cima = nuevoNodo
    pila.tamanio += 1


def desapilar(pila):
    info = pila.cima.info
    pila.cima = pila.cima.siguiente
    pila.tamanio -= 1
    return info


def esVacia(pila):
    return pila.cima is None


def imprimir(pila):
    pilaAuxiliar = Pila()
    while not esVacia(pila):
        info = desapilar(pila)
        print(info)
        apilar(pilaAuxiliar, info)
    while not esVacia(pilaAuxiliar):
        info = desapilar(pilaAuxiliar)
        apilar(pila, info)


def enCima(pila):
    if pila.cima is not None:
        return pila.cima.info
    else:
        return None


def index_de_pila(pila, parametro):
    pilaAuxiliar = Pila()
    index = 0
    existe = True
    while enCima(pila) != parametro:
        if enCima(pila) == None:
            existe = False
            break
        info = desapilar(pila)
        apilar(pilaAuxiliar, info)
        index += 1
    while not esVacia(pilaAuxiliar):
        info = desapilar(pilaAuxiliar)
        apilar(pila, info)
    if existe == True:
        return index
    else:
        return None
