class nodoCola(object):
    info, siguiente, prioridad = None, None, None


class Cola(object):
    def __init__(self):
        self.entrada, self.salida = None, None
        self.tamanio = 0


    def arribo(self, info, prioridad):
        nuevoNodo = nodoCola()
        nuevoNodo.info = info
        nuevoNodo.prioridad = prioridad
        if self.salida is None:
            self.salida = nuevoNodo
            self.entrada = nuevoNodo
        else:
            actual = self.salida
            siguiente = actual.siguiente
            while prioridad <= actual.prioridad:
                if prioridad > actual.prioridad:
                    self.salida.siguiente = actual
                    self.salida = nuevoNodo
                    break
                elif siguiente == None:
                    self.entrada.siguiente = nuevoNodo
                    self.entrada = nuevoNodo
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
        self.tamanio += 1


    def atencion(self):
        info = self.salida.info
        prio = self.salida.prioridad
        self.salida = self.salida.siguiente
        if self.salida is None:
            self.entrada = None
        self.tamanio -= 1
        return info, prio


    def esVacia(self):
        return self.entrada is None


    def imprimir(self):
        colaAuxiliar = Cola()
        while not self.esVacia():
            info, prioridad = self.atencion
            print(info)
            colaAuxiliar.arribo(info, prioridad)
        while not colaAuxiliar.esVacia():
            info, prioridad = colaAuxiliar.atencion()
            self.arribo(info, prioridad)


    def index_of(self, parametro):
        colaAuxiliar = Cola()
        index = 0
        existe = False
        while not self.esVacia():
            if self.salida.info != parametro:
                index += 1
            else:
                existe = True
            info, prioridad = self.atencion()
            colaAuxiliar.arribo(info, prioridad)
        while not colaAuxiliar.esVacia():
            info, prioridad = colaAuxiliar.atencion()
            self.arribo(info, prioridad)
        if existe == True:
            return index
        else:
            return None
