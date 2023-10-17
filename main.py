import time
import csv
import random
from pokemon import Pokemon
from lista import Lista
from cola_prioridad import Cola
from arbol import nodoArbol
from grafo import Grafo


def crear_lista():
    # Abrir el archivo y pasarlo a una lista propia
    with open("Pokemon.csv") as tsvF:
        lista_pokemon = Lista()
        for i in range(1195):
            reader = csv.reader(tsvF)
            encabezado = next(reader)
            if i > 0:
                nuevo = Pokemon(encabezado[0], encabezado[1], encabezado[11])
                tipos = Lista()
                tipos.insertar(encabezado[2])
                tipos.insertar(encabezado[3])
                nuevo.set_tipo(tipos)
                stats = Lista()
                for j in range(4, 11):
                    stats.insertar(encabezado[j])
                nuevo.set_stats(stats)
                lista_pokemon.insertar(nuevo)
    return lista_pokemon


def crear_cola(lista_pokemon):
    # Crea la cola de pokemon segun sus STATS totales
    cola = Cola()
    while cola.get_tamanio() < 100:
        indice = random.randint(0, lista_pokemon.tamanio - 1)
        if cola.existe(lista_pokemon.index(indice)) == False:
            cola.arribo(lista_pokemon.index(indice), int(lista_pokemon.index(indice).get_stats().index(0)))
    return cola


def crear_arbol(lista_pokemon):
    # Crea el arbol segun los STAS totales
    indice = random.randint(0, lista_pokemon.tamanio - 1)
    raiz = nodoArbol(lista_pokemon.index(indice))
    lista_chiquita = Lista()
    cont = 0
    while cont < 300:
        indice = random.randint(0, lista_pokemon.tamanio - 1)
        if raiz.existe(lista_pokemon.index(indice)) == False:
            raiz.insertarNodo(lista_pokemon.index(indice))
            lista_chiquita.insertar(lista_pokemon.index(indice))
            cont += 1
    return raiz, lista_chiquita


def crear_grafo(lista_pokemon):
    tabla_tipos = Grafo()
    for i in range(lista_pokemon.tamanio):
        tabla_tipos.insertarVertice(lista_pokemon.index(i))

    for j in range(lista_pokemon.tamanio):
        print(j)
        for c in range(lista_pokemon.tamanio):
            tabla_tipos.insertarArista(tabla_tipos.buscarVertice(lista_pokemon.index(j)), tabla_tipos.buscarVertice(lista_pokemon.index(c)))


    print(tabla_tipos.tamanio)
    print(tabla_tipos.imprimirPorAmplitud(tabla_tipos.buscarVertice(lista_pokemon.index(0))))



def main():
    # Abrir el archivo y pasarlo a una lista propia
    lista_pokemon = crear_lista()
    cola_pokemon = crear_cola(lista_pokemon)
    arbol_pokemon, lista_chiquita = crear_arbol(lista_pokemon)
    crear_grafo(lista_pokemon)
    #arbol_pokemon.imprimirPostOrden()

    """indice = random.randint(0, lista_chiquita.tamanio - 1)
    ini_1  = time.time()
    print(lista_chiquita.index_of(lista_chiquita.index(indice)))
    fin_1 = time.time()
    print(fin_1 - ini_1)
    ini_2 = time.time()
    print(arbol_pokemon.existe(lista_chiquita.index(indice)))
    fin_2 = time.time()
    print(fin_2 - ini_2)"""
    """
    print(lista_pokemon.index(0).get_generacion())
    print("---------------------")
    print(lista_pokemon.index_of("Charmander"))
    print("-------------------------")
    lista_pokemon.index_of('413').imprimir()
    print("------------------------")
    lista_pokemon.index_of('Dragon').imprimir()
    print("--------------------------")
    lista_pokemon.index_of('gen1').imprimir()
    """


    # Busqueda por un atributo
        # Nombre
        # Numero de la pokedex
        # tipo
        # Generacion
    # Generacion una Cola por prioridad de generacion de 100 elementos
    # Generacion un Arbol Binario con 300 pokemons aleatorios ordenados por pokedex


if __name__ == "__main__":
    main()