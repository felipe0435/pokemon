from cola import Cola

class nodoArista(object):
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.siguiente = None


class nodoVertice(object):
    def __init__(self, info):
        self.info = info
        self.siguiente = None
        self.visitado = False
        self.adyacentes = Arista()


class Arista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


class Grafo(object):
    def __init__(self, dirigido=True):
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0


    def insertarVertice(self, info):
        nodo = nodoVertice(info)
        if self.inicio is None:
            nodo.siguiente = self.inicio
            self.inicio = nodo
        else:
            ant = self.inicio
            act = self.inicio.siguiente
            while act is not None:
                ant = act
                act = act.siguiente
            nodo.siguiente = act
            ant.siguiente = nodo
        self.tamanio += 1


    def agregarArista(origen, info, destino):
        nodo = nodoArista(info, destino)
        if origen.inicio is None or origen.inicio.destino > destino:
            nodo.siguiente = origen.inicio
            origen.inicio = nodo
        else:
            ant = origen.inicio
            act = origen.inicio.siguiente
            while act is not None and act.destino < nodo.destino:
                ant = act
                act = act.siguiente
            nodo.siguiente = act
            ant.siguiente = nodo
        origen.tamanio += 1


    def insertarArista(self, info, origen, destino):
        self.agregarArista(origen.adyacentes, info, destino.info)
        if not self.dirigido:
            self.agregarArista(destino.adyacentes, info, origen.info)


    def eliminarArista(vertice, destino):
        x = None
        if vertice.inicio.destino == destino:
            x = vertice.inicio.info
            vertice.inicio = vertice.inicio.siguiente
            vertice.tamanio -= 1
        else:
            ant = vertice.inicio
            act = vertice.inicio.siguiente
            while act is not None and act.destino != destino:
                ant = act
                act = act.siguiente
            if act is not None:
                x = act.info
                ant.siguiente = act.siguiente
                vertice.tamanio -= 1
            return x


    def eliminarVertice(self, info):
        x = None
        if self.inicio.info == info:
            x = self.inicio.info
            self.inicio = self.inicio.siguiente
            self.tamanio -= 1
        else:
            ant = self.inicio
            act = self.inicio.siguiente
            while act is not None and act.info != info:
                ant = act
                act = act.siguiente
            if act is not None:
                x = act.info
                ant.siguiente = act.siguiente
                self.tamanio -= 1
        if x is not None:
            aux = self.inicio
            while aux is not None:
                if aux.adyacentes.inicio is not None:
                    self.eliminarArista(aux.adyacentes, info)
                aux = aux.siguiente
        return x


    def tamanio(self):
        return self.tamanio


    def grafoVacio(self):
        return self.inicio in None


    def buscarVertice(self, info):
        aux = self.inicio
        while aux is not None and aux.info != info:
            aux = aux.siguiente
        return aux


    def buscarArista(vertice, info):
        aux = vertice.adyacentes.inicio
        while aux is not None and aux.info != info:
            aux = aux.siguiente
        return aux


    def existePaso(self, origen, destino):
        resultado = False
        if not origen.visitado:
            origen.visitado = True
            verticesAdyacentes = origen.adyacentes.inicio
            while verticesAdyacentes is not None and not resultado:
                adyacente = self.buscarVertice(verticesAdyacentes.destino)
                if adyacente.info == destino.info:
                    return True
                elif not adyacente.visitado:
                    resultado = self.existePaso(adyacente, destino)
                verticesAdyacentes = verticesAdyacentes.siguiente
        return resultado


    def adyacentes(vertice):
        if vertice is None:
            return None
        aux = vertice.adyacentes.inicio
        while aux is not None:
            print(aux.destino, aux.info)
            aux = aux.siguiente


    def esAdyacente(vertice, destino):
        resultado = False
        aux = vertice.adyacentes.inicio
        while aux is not None and not resultado:
            if aux.destino == resultado:
                resultado = True
            aux = aux.siguiente
        return resultado


    def marcarNoVisitado(self):
        aux = self.inicio
        while aux is not None:
            aux.visitado = False
            aux = aux.siguiente


    def imprimirVertices(self):
        aux = self.inicio
        while aux is not None:
            print(aux.info)
            aux = aux.siguiente


    def imprimirPorProfundidad(self, vertice):
        while vertice is not None:
            if not vertice.visitado:
                vertice.visitado = True
                print(vertice.info)
                adyacentes = vertice.adyacentes.inicio
                while adyacentes is not None:
                    adyacente = self.buscarVertice(adyacentes.destino)
                    if not adyacente.visitado:
                        self.imprimirPorProfundidad(adyacente)
                    adyacentes = adyacentes.siguiente
            vertice = vertice.siguiente


    def imprimirPorAmplitud(self, vertice):
        cola = Cola()
        while vertice is not None:
            if not vertice.visitado:
                vertice.visitado = True
                cola.arribo(vertice)
                while not cola.esVacia():
                    nodo = cola.atencion()
                    print(nodo.info)
                    adyacentes = nodo.adyacentes.inicio
                    while adyacentes is not None:
                        adyacente = self.buscarVertice(adyacentes.destino)
                        if not adyacente.visitado:
                            adyacente.visitado = True
                            cola.arribo(adyacente)
                        adyacentes = adyacentes.siguiente
            vertice = vertice.siguiente


    def multiplicador(self, tipo1, tipo2):
        total = 0
        for i in range(2):
            multiplicador = 1
            match tipo1.index(i):
                case "Grass":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                multiplicador /= 2
                            case "Fire":
                                multiplicador /= 2
                            case "Water":
                                multiplicador *= 2
                            case "Bug":
                                multiplicador /= 2
                            case "Normal":
                                pass
                            case "Poison":
                                multiplicador /= 2
                            case "Electric":
                                pass
                            case "Ground":
                                multiplicador *= 2
                            case "Fairy":
                                pass
                            case "Steel":
                                multiplicador /= 2
                            case "Dragon":
                                multiplicador /= 2
                            case "Ghost":
                                pass
                            case "Ice":
                                pass
                            case "Fighting":
                                pass
                            case "Psychic":
                                pass
                            case "Rock":
                                multiplicador *= 2
                            case "Dark":
                                pass
                            case "Flying":
                                multiplicador /= 2
                            case _ :
                                pass
                case "Fire":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                multiplicador *= 2
                            case "Fire":
                                multiplicador /= 2
                            case "Water":
                                multiplicador /= 2
                            case "Bug":
                                multiplicador *= 2
                            case "Normal":
                                pass
                            case "Poison":
                                pass
                            case "Electric":
                                pass
                            case "Ground":
                                pass
                            case "Fairy":
                                pass
                            case "Steel":
                                multiplicador *= 2
                            case "Dragon":
                                multiplicador /= 2
                            case "Ghost":
                                pass
                            case "Ice":
                                multiplicador *= 2
                            case "Fighting":
                                pass
                            case "Psychic":
                                pass
                            case "Rock":
                                multiplicador /= 2
                            case "Dark":
                                pass
                            case "Flying":
                                pass
                            case _ :
                                pass
                case "Water":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                multiplicador /= 2
                            case "Fire":
                                multiplicador *= 2
                            case "Water":
                                multiplicador /= 2
                            case "Bug":
                                pass
                            case "Normal":
                                pass
                            case "Poison":
                                pass
                            case "Electric":
                                pass
                            case "Ground":
                                multiplicador *= 2
                            case "Fairy":
                                pass
                            case "Steel":
                                pass
                            case "Dragon":
                                multiplicador /= 2
                            case "Ghost":
                                pass
                            case "Ice":
                                pass
                            case "Fighting":
                                pass
                            case "Psychic":
                                pass
                            case "Rock":
                                multiplicador *= 2
                            case "Dark":
                                pass
                            case "Flying":
                                pass
                            case _ :
                                pass
                case "Bug":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                multiplicador *= 2
                            case "Fire":
                                multiplicador /= 2
                            case "Water":
                                pass
                            case "Bug":
                                pass
                            case "Normal":
                                pass
                            case "Poison":
                                multiplicador /= 2
                            case "Electric":
                                pass
                            case "Ground":
                                pass
                            case "Fairy":
                                multiplicador /= 2
                            case "Steel":
                                multiplicador /= 2
                            case "Dragon":
                                pass
                            case "Ghost":
                                multiplicador /= 2
                            case "Ice":
                                pass
                            case "Fighting":
                                multiplicador /= 2
                            case "Psychic":
                                multiplicador *= 2
                            case "Rock":
                                pass
                            case "Dark":
                                multiplicador *= 2
                            case "Flying":
                                multiplicador /= 2
                            case _ :
                                pass
                case "Normal":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                pass
                            case "Fire":
                                pass
                            case "Water":
                                pass
                            case "Bug":
                                pass
                            case "Normal":
                                pass
                            case "Poison":
                                pass
                            case "Electric":
                                pass
                            case "Ground":
                                pass
                            case "Fairy":
                                pass
                            case "Steel":
                                multiplicador /= 2
                            case "Dragon":
                                pass
                            case "Ghost":
                                multiplicador = 0
                            case "Ice":
                                pass
                            case "Fighting":
                                pass
                            case "Psychic":
                                pass
                            case "Rock":
                                multiplicador /= 2
                            case "Dark":
                                pass
                            case "Flying":
                                pass
                            case _ :
                                pass
                case "Poison":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                multiplicador *= 2
                            case "Fire":
                                pass
                            case "Water":
                                pass
                            case "Bug":
                                pass
                            case "Normal":
                                pass
                            case "Poison":
                                multiplicador /= 2
                            case "Electric":
                                pass
                            case "Ground":
                                multiplicador /= 2
                            case "Fairy":
                                multiplicador *= 2
                            case "Steel":
                                multiplicador = 0
                            case "Dragon":
                                pass
                            case "Ghost":
                                multiplicador /= 2
                            case "Ice":
                                pass
                            case "Fighting":
                                pass
                            case "Psychic":
                                pass
                            case "Rock":
                                multiplicador /= 2
                            case "Dark":
                                pass
                            case "Flying":
                                pass
                            case _ :
                                pass
                case "Electric":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                multiplicador /= 2
                            case "Fire":
                                pass
                            case "Water":
                                multiplicador *= 2
                            case "Bug":
                                pass
                            case "Normal":
                                pass
                            case "Poison":
                                pass
                            case "Electric":
                                multiplicador /= 2
                            case "Ground":
                                multiplicador = 0
                            case "Fairy":
                                pass
                            case "Steel":
                                pass
                            case "Dragon":
                                multiplicador /= 2
                            case "Ghost":
                                pass
                            case "Ice":
                                pass
                            case "Fighting":
                                pass
                            case "Psychic":
                                pass
                            case "Rock":
                                pass
                            case "Dark":
                                pass
                            case "Flying":
                                multiplicador *= 2
                            case _ :
                                pass
                case "Ground":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                multiplicador /= 2
                            case "Fire":
                                multiplicador *= 2
                            case "Water":
                                pass
                            case "Bug":
                                pass
                            case "Normal":
                                pass
                            case "Poison":
                                multiplicador *= 2
                            case "Electric":
                                multiplicador *= 2
                            case "Ground":
                                pass
                            case "Fairy":
                                pass
                            case "Steel":
                                multiplicador *= 2
                            case "Dragon":
                                multiplicador /= 2
                            case "Ghost":
                                pass
                            case "Ice":
                                pass
                            case "Fighting":
                                pass
                            case "Psychic":
                                pass
                            case "Rock":
                                multiplicador *= 2
                            case "Dark":
                                pass
                            case "Flying":
                                multiplicador = 0
                            case _ :
                                pass
                case "Fairy":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                pass
                            case "Fire":
                                multiplicador /= 2
                            case "Water":
                                pass
                            case "Bug":
                                pass
                            case "Normal":
                                pass
                            case "Poison":
                                multiplicador /= 2
                            case "Electric":
                                pass
                            case "Ground":
                                pass
                            case "Fairy":
                                pass
                            case "Steel":
                                multiplicador /= 2
                            case "Dragon":
                                multiplicador *= 2
                            case "Ghost":
                                pass
                            case "Ice":
                                pass
                            case "Fighting":
                                multiplicador *= 2
                            case "Psychic":
                                pass
                            case "Rock":
                                pass
                            case "Dark":
                                multiplicador *= 2
                            case "Flying":
                                pass
                            case _ :
                                pass
                case "Steel":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                pass
                            case "Fire":
                                multiplicador /= 2
                            case "Water":
                                multiplicador /= 2
                            case "Bug":
                                pass
                            case "Normal":
                                pass
                            case "Poison":
                                pass
                            case "Electric":
                                multiplicador /= 2
                            case "Ground":
                                pass
                            case "Fairy":
                                multiplicador *= 2
                            case "Steel":
                                multiplicador /= 2
                            case "Dragon":
                                pass
                            case "Ghost":
                                pass
                            case "Ice":
                                multiplicador *= 2
                            case "Fighting":
                                pass
                            case "Psychic":
                                pass
                            case "Rock":
                                multiplicador *= 2
                            case "Dark":
                                pass
                            case "Flying":
                                pass
                            case _ :
                                pass
                case "Dragon":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                pass
                            case "Fire":
                                pass
                            case "Water":
                                pass
                            case "Bug":
                                pass
                            case "Normal":
                                pass
                            case "Poison":
                                pass
                            case "Electric":
                                pass
                            case "Ground":
                                pass
                            case "Fairy":
                                multiplicador = 0
                            case "Steel":
                                multiplicador /= 2
                            case "Dragon":
                                multiplicador *= 2
                            case "Ghost":
                                pass
                            case "Ice":
                                pass
                            case "Fighting":
                                pass
                            case "Psychic":
                                pass
                            case "Rock":
                                pass
                            case "Dark":
                                pass
                            case "Flying":
                                pass
                            case _ :
                                pass
                case "Ghost":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                pass
                            case "Fire":
                                pass
                            case "Water":
                                pass
                            case "Bug":
                                pass
                            case "Normal":
                                multiplicador = 0
                            case "Poison":
                                pass
                            case "Electric":
                                pass
                            case "Ground":
                                pass
                            case "Fairy":
                                pass
                            case "Steel":
                                pass
                            case "Dragon":
                                pass
                            case "Ghost":
                                multiplicador *= 2
                            case "Ice":
                                pass
                            case "Fighting":
                                pass
                            case "Psychic":
                                multiplicador *= 2
                            case "Rock":
                                pass
                            case "Dark":
                                multiplicador /= 2
                            case "Flying":
                                pass
                            case _ :
                                pass
                case "Ice":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                multiplicador *= 2
                            case "Fire":
                                multiplicador /= 2
                            case "Water":
                                multiplicador /= 2
                            case "Bug":
                                pass
                            case "Normal":
                                pass
                            case "Poison":
                                pass
                            case "Electric":
                                pass
                            case "Ground":
                                multiplicador *= 2
                            case "Fairy":
                                pass
                            case "Steel":
                                multiplicador /= 2
                            case "Dragon":
                                multiplicador *= 2
                            case "Ghost":
                                pass
                            case "Ice":
                                multiplicador /= 2
                            case "Fighting":
                                pass
                            case "Psychic":
                                pass
                            case "Rock":
                                pass
                            case "Dark":
                                pass
                            case "Flying":
                                multiplicador *= 2
                            case _ :
                                pass
                case "Fighting":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                pass
                            case "Fire":
                                pass
                            case "Water":
                                pass
                            case "Bug":
                                multiplicador /= 2
                            case "Normal":
                                multiplicador *= 2
                            case "Poison":
                                multiplicador /= 2
                            case "Electric":
                                pass
                            case "Ground":
                                pass
                            case "Fairy":
                                multiplicador /= 2
                            case "Steel":
                                multiplicador *= 2
                            case "Dragon":
                                pass
                            case "Ghost":
                                multiplicador = 0
                            case "Ice":
                                multiplicador *= 2
                            case "Fighting":
                                pass
                            case "Psychic":
                                multiplicador /= 2
                            case "Rock":
                                multiplicador *= 2
                            case "Dark":
                                multiplicador *= 2
                            case "Flying":
                                multiplicador /= 2
                            case _ :
                                pass
                case "Psychic":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                pass
                            case "Fire":
                                pass
                            case "Water":
                                pass
                            case "Bug":
                                pass
                            case "Normal":
                                pass
                            case "Poison":
                                multiplicador *= 2
                            case "Electric":
                                pass
                            case "Ground":
                                pass
                            case "Fairy":
                                pass
                            case "Steel":
                                multiplicador /= 2
                            case "Dragon":
                                pass
                            case "Ghost":
                                pass
                            case "Ice":
                                pass
                            case "Fighting":
                                multiplicador *= 2
                            case "Psychic":
                                multiplicador /= 2
                            case "Rock":
                                pass
                            case "Dark":
                                multiplicador = 0
                            case "Flying":
                                pass
                            case _ :
                                pass
                case "Rock":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                pass
                            case "Fire":
                                multiplicador *= 2
                            case "Water":
                                pass
                            case "Bug":
                                multiplicador *= 2
                            case "Normal":
                                pass
                            case "Poison":
                                pass
                            case "Electric":
                                pass
                            case "Ground":
                                multiplicador /= 2
                            case "Fairy":
                                pass
                            case "Steel":
                                multiplicador /= 2
                            case "Dragon":
                                pass
                            case "Ghost":
                                pass
                            case "Ice":
                                multiplicador *= 2
                            case "Fighting":
                                multiplicador /= 2
                            case "Psychic":
                                pass
                            case "Rock":
                                pass
                            case "Dark":
                                pass
                            case "Flying":
                                multiplicador *= 2
                            case _ :
                                pass
                case "Dark":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                pass
                            case "Fire":
                                pass
                            case "Water":
                                pass
                            case "Bug":
                                pass
                            case "Normal":
                                pass
                            case "Poison":
                                pass
                            case "Electric":
                                pass
                            case "Ground":
                                pass
                            case "Fairy":
                                multiplicador /= 2
                            case "Steel":
                                pass
                            case "Dragon":
                                pass
                            case "Ghost":
                                multiplicador *= 2
                            case "Ice":
                                pass
                            case "Fighting":
                                multiplicador /= 2
                            case "Psychic":
                                multiplicador *= 2
                            case "Rock":
                                pass
                            case "Dark":
                                multiplicador /= 2
                            case "Flying":
                                pass
                            case _ :
                                pass
                case "Flying":
                    for j in range(2):
                        match tipo2.index(j):
                            case "Grass":
                                multiplicador *= 2
                            case "Fire":
                                pass
                            case "Water":
                                pass
                            case "Bug":
                                multiplicador *= 2
                            case "Normal":
                                pass
                            case "Poison":
                                pass
                            case "Electric":
                                multiplicador /= 2
                            case "Ground":
                                pass
                            case "Fairy":
                                pass
                            case "Steel":
                                multiplicador /= 2
                            case "Dragon":
                                pass
                            case "Ghost":
                                pass
                            case "Ice":
                                pass
                            case "Fighting":
                                multiplicador *= 2
                            case "Psychic":
                                pass
                            case "Rock":
                                multiplicador /= 2
                            case "Dark":
                                pass
                            case "Flying":
                                pass
                            case _ :
                                pass
                case _ :
                    multiplicador = 0
            total += multiplicador

        return total
