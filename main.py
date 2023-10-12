import csv
import random
from pokemon import Pokemon
from lista import Lista
from cola_prioridad import Cola


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
    cola = Cola()
    while cola.get_tamanio() < 100:
        indice = random.randint(0, lista_pokemon.tamanio - 1)
        if cola.existe(lista_pokemon.index(indice)) == False:
            cola.arribo(lista_pokemon.index(indice), int(lista_pokemon.index(indice).get_id()))

    return cola


def main():
    # Abrir el archivo y pasarlo a una lista propia
    lista_pokemon = crear_lista()
    cola_pokemon = crear_cola(lista_pokemon)
    cola_pokemon.imprimir()
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