import csv
from pokemon import Pokemon
from lista import Lista


with open("Pokemon.csv") as tsvF:
    lista_pokemon = Lista()
    for i in range(1195):
        reader = csv.reader(tsvF)
        encabezado = next(reader)
        if i > 0:
            print(encabezado)
            nuevo = Pokemon(encabezado[0], encabezado[1], encabezado[2], encabezado[12])
            tipos = Lista()
            tipos.insertar(encabezado[3])
            tipos.insertar(encabezado[4])
            nuevo.set_tipo(tipos)
            stats = Lista()
            for c in range(5, 12):
                stats.insertar(encabezado[c])
            nuevo.set_stats(stats)
            nuevo.get_stats().imprimir()
            lista_pokemon.insertar(nuevo)
    lista_pokemon.imprimir()