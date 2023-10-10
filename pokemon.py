from lista import Lista

class Pokemon():
    def __init__(self, id, nombre, forma, gen):
        self.__id = id
        self.__nombre = nombre
        self.__forma = forma
        self.__tipo = None
        self.__stats = None
        self.__generacion = gen


    def set_tipo(self, tipo):
        self.__tipo = tipo


    def get_tipo(self):
        return self.__tipo


    def set_stats(self, stats):
        self.__stats = stats


    def get_stats(self):
        return self.__stats

