from arbol import nodoArbol

raiz = nodoArbol("J")

raiz.insertarNodo("B")
raiz.insertarNodo("C")
raiz.insertarNodo("K")
raiz.insertarNodo("O")

raiz.imprimirInOrden()
print("--------------------------------")
raiz.imprimirPostOrden()
print("--------------------------------")
raiz.imprimirPreOrden()