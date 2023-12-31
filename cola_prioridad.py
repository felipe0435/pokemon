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
            while True:
                if prioridad >= actual.prioridad and siguiente == None:
                    actual.siguiente = nuevoNodo
                    self.entrada = nuevoNodo
                    break
                elif prioridad < self.salida.prioridad:
                    nuevoNodo.siguiente = self.salida
                    self.salida = nuevoNodo
                    break
                elif prioridad >= actual.prioridad and prioridad < siguiente.prioridad:
                    nuevoNodo.siguiente = siguiente
                    actual.siguiente = nuevoNodo
                    break
                elif prioridad < actual.prioridad:
                    nuevoNodo.siguiente = actual
                    nuevoNodo.salida = nuevoNodo
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
        cont = 0
        while not self.esVacia():
            cont += 1
            info, prioridad = self.atencion()
            print(info.get_nombre(), prioridad)
            colaAuxiliar.arribo(info, prioridad)
        while not colaAuxiliar.esVacia():
            info, prioridad = colaAuxiliar.atencion()
            self.arribo(info, prioridad)


    def index_of(self, parametro):
        # Busca un pokemon segun su nombre y devuelve su lugar en la lista
        colaAuxiliar = Cola()
        index = 0
        existe = False
        while not self.esVacia():
            if self.salida.info != parametro and self.salida.info.get_nombre() != parametro:
                index += 1
            else:
                existe = True
            info, prioridad = self.atencion()
            colaAuxiliar.arribo(info, prioridad)
        while not colaAuxiliar.esVacia():
            info, prioridad = colaAuxiliar.atencion()
            self.arribo(info, prioridad)
        if existe == True:
            return index, existe
        else:
            return None, existe


    def existe(self, parametro):
        # Dice si existe o no el nombre del pokemon en la cola
        colaAuxiliar = Cola()
        existe = False
        while not self.esVacia():
            if self.salida.info == parametro or self.salida.info.get_nombre() == parametro:
                existe = True
            info, prioridad = self.atencion()
            colaAuxiliar.arribo(info, prioridad)
        while not colaAuxiliar.esVacia():
            info, prioridad = colaAuxiliar.atencion()
            self.arribo(info, prioridad)
        return existe


    def get_tamanio(self):
        # Dice el tamanio de la cola
        return self.tamanio
