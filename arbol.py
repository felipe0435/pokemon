from cola import Cola

class nodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info


    def insertarNodo(self, data):
        if(data.get_nombre() < self.info.get_nombre()) and self.izq == None:
            self.izq = nodoArbol(data)
        elif(data.get_nombre() < self.info.get_nombre()) and self.izq != None:
            self.izq = self.izq.insertarNodo(data)
        elif (data.get_nombre() >= self.info.get_nombre()) and self.der == None:
            self.der = nodoArbol(data)
        elif (data.get_nombre() >= self.info.get_nombre()) and self.der != None:
            self.der = self.der.insertarNodo(data)
        return self


    def arbolVacio(self, raiz):
        return raiz is None


    def remplazar(self, raiz):
        aux = None
        if(raiz.der is None):
            aux = raiz
            raiz = raiz.izq
        else:
            raiz.der, aux = self.remplazar(raiz.der)
        return raiz, aux


    def eliminarNodo(self, raiz, info):
        x = None
        if(raiz is not None):
            if(info<raiz.info):
                raiz.izq, x = self.eliminarNodo(raiz.izq,info)
            elif(info>raiz.info):
                raiz.der, x = self.eliminarNodo(raiz.der,info)
            else:
                x=raiz.info
                if(raiz.izq is None):
                    raiz = raiz.der
                elif(raiz.der is None):
                    raiz = raiz.izq
                else:
                    raiz.izq, aux = self.remplazar(raiz.izq)
                    raiz.info = aux.info
        return raiz, x


    def buscar(self, raiz, info):
        existe = False
        if raiz is not None:
            if existe == True:
                pass
            return raiz, info
        elif(raiz.info == info):
            return raiz.info
        elif(raiz.izq < info):
            return self.buscar(raiz.izq, info)
        elif(raiz.der > info):
            return self.buscar(raiz.der, info)
        else:
            return None


    def imprimirPorNivel(self, raiz):
        pendientes = Cola()
        pendientes.arribo(pendientes, raiz)
        while(not self.esVacia(pendientes)):
            nodo = pendientes.atencion(pendientes)
            print(nodo.info)
            if(nodo.izq is not None):
                pendientes.arribo(pendientes, nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(pendientes, nodo.der)


    def imprimirInOrden(self):
        if(self.info is not None):
            if self.izq != None:
                self.izq.imprimirInOrden()
            print(self.info.get_nombre())
            if self.der != None:
                self.der.imprimirInOrden()


    def imprimirPreOrden(self):
        if(self.info is not None):
            print(self.info.get_nombre())
            if self.der != None:
                self.der.imprimirPreOrden()
            if self.izq != None:
                self.izq.imprimirPreOrden()


    def imprimirPostOrden(self):
        if(self.info is not None):
            if self.izq != None:
                self.izq.imprimirPostOrden()
            if self.der != None:
                self.der.imprimirPostOrden()
            print(self.info.get_nombre())


    def existe(self, data):
        if data.get_nombre() == self.info.get_nombre():
            return True
        elif data.get_nombre() < self.info.get_nombre() and self.izq == None:
           return False
        elif data.get_nombre() > self.info.get_nombre() and self.der == None:
            return False
        elif data.get_nombre() < self.info.get_nombre():
            return self.izq.existe(data)
        elif data.get_nombre() > self.info.get_nombre():
            return self.der.existe(data)

