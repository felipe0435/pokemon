class nodoCola(object):
    info, siguiente = None, None


class Cola(object):
    def __init__(self):
        self.entrada, self.salida = None, None
        self.tamanio = 0


    def arribo(self, info):
        nuevoNodo = nodoCola()
        nuevoNodo.info = info
        if self.salida is None:
            self.salida = nuevoNodo
        else:
            self.entrada.siguiente = nuevoNodo
        self.entrada = nuevoNodo
        self.tamanio += 1


    def atencion(self):
        info = self.salida.info
        self.salida = self.salida.siguiente
        if self.salida is None:
            self.entrada = None
        self.tamanio -= 1
        return info


    def esVacia(self):
        return self.entrada is None


    def imprimir(self):
        colaAuxiliar = Cola()
        while not self.esVacia():
            info = self.atencion()
            print(info)
            colaAuxiliar.arribo(info)
        while not colaAuxiliar.esVacia():
            info = colaAuxiliar.esVacia()
            self.arribo(info)


    def index_of(self, parametro):
        colaAuxiliar = Cola()
        index = 0
        existe = False
        while not self.esVacia():
            if self.salida.info != parametro:
                index += 1
            else:
                existe = True
            info = self.atencion()
            colaAuxiliar.arribo(info)
        while not colaAuxiliar.esVacia():
            info = colaAuxiliar.atencion()
            self.arribo(info)
        if existe == True:
            return index
        else:
            return None
