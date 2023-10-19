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
    cont = 1
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
            tabla_tipos.insertarArista(tabla_tipos.buscarVertice(lista_pokemon.index(j)),
                                       tabla_tipos.buscarVertice(lista_pokemon.index(c)))

    return tabla_tipos


def main():
    # Abrir el archivo y pasarlo a una lista propia
    lista_pokemon = crear_lista()
    cola_pokemon = crear_cola(lista_pokemon)
    arbol_pokemon, lista_chiquita = crear_arbol(lista_pokemon)

    lista_tiempos = Lista()
    prom = 0
    """
    for _ in range(10):
        ini_grafo = time.time()
        tabla_tipos = crear_grafo(lista_pokemon)
        fin_grafo = time.time()
        tot_grafo = fin_grafo - ini_grafo
        prom += tot_grafo
        lista_tiempos.insertar(tot_grafo)
    prom /= 10
    lista_tiempos.insertar(prom)
    lista_tiempos.imprimir()
    """
    #arbol_pokemon.imprimirPostOrden()

    tiempos_lista = Lista()
    tiempos_arbol = Lista()
    tot_l = 0
    tot_a = 0
    for _ in range(10):
        indice = random.randint(0, lista_chiquita.tamanio - 1)
        ini_1  = time.time()
        lista_chiquita.index_of(lista_chiquita.index(indice))
        fin_1 = time.time()
        tiempo_l = fin_1 - ini_1
        ini_2 = time.time()
        arbol_pokemon.existe(lista_chiquita.index(indice))
        fin_2 = time.time()
        tiempo_a = fin_2 - ini_2
        tiempos_lista.insertar(tiempo_l)
        tot_l += tiempo_l
        tiempos_arbol.insertar(tiempo_a)
        tot_a += tiempo_a
    tot_l /= 10
    tot_a /= 10
    tiempos_lista.insertar(tot_l)
    tiempos_arbol.insertar(tot_a)

    tiempos_lista.imprimir()
    print("-------------------------------------")
    tiempos_arbol.imprimir()
    print("-------------------------------------")


    tiempos_cola = Lista()
    tot_cola = 0
    for _ in range(10):
        indice = random.randint(0, lista_chiquita.tamanio - 1)
        ini_cola = time.time()
        print(cola_pokemon.index_of(lista_pokemon.index(indice)))
        fin_cola = time.time()
        tiempo_cola = fin_cola - ini_cola
        tiempos_cola.insertar(tiempo_cola)
        tot_cola += tiempo_cola
    tot_cola /= 10
    tiempos_cola.insertar(tot_cola)
    tiempos_cola.imprimir()


    print(lista_pokemon.index(0).get_nombre())
    print("--------------------------")
    print(lista_pokemon.index_of("Charmander"))
    print("--------------------------")
    lista_pokemon.index_of('413').imprimir()
    print("--------------------------")
    lista_pokemon.index_of('Dragon').imprimir()
    print("--------------------------")
    lista_pokemon.index_of('gen1').imprimir()
    print("---------------------------")

    """
    tabla_tipos.get_adyacentes(tabla_tipos.buscarVertice("Charmander"))
    print("---------------------------")
    tabla_tipos.get_adyacentes(tabla_tipos.buscarVertice("Eevee"))
    print("---------------------------")
    tabla_tipos.get_adyacentes(tabla_tipos.buscarVertice("Machop"))
    print("---------------------------")
    print(fin_grafo - ini_grafo)
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