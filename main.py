import csv
from pokemon import Pokemon
from lista import Lista


def main():
    # Abrir el archivo y pasarlo a una lista propia
    with open("Pokemon.csv") as tsvF:
        lista_pokemon = Lista()
        for i in range(1195):
            reader = csv.reader(tsvF)
            encabezado = next(reader)
            if i > 0:
                nuevo = Pokemon(encabezado[0], encabezado[1], encabezado[2], encabezado[12])
                tipos = Lista()
                tipos.insertar(encabezado[3])
                tipos.insertar(encabezado[4])
                nuevo.set_tipo(tipos)
                stats = Lista()
                for j in range(5, 12):
                    stats.insertar(encabezado[j])
                nuevo.set_stats(stats)
                lista_pokemon.insertar(nuevo)

    print(lista_pokemon.index(0).get_id())
    print("---------------------")
    print(lista_pokemon.index_of("Charmander"))
    print("-------------------------")
    lista_pokemon.index_of('6').imprimir()
    print("------------------------")
    lista_pokemon.index_of('Dragon').imprimir()
    print("--------------------------")
    lista_pokemon.index_of('1')
    # Busqueda por un atributo
        # Nombre
        # Numero de la pokedex
        # tipo
        # Generacion
    # Generacion una Cola por prioridad de generacion de 100 elementos
    # Generacion un Arbol Binario con 300 pokemons aleatorios ordenados por pokedex



if __name__ == "__main__":
    main()