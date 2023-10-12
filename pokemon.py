from lista import Lista

class Pokemon():
    def __init__(self, id, nombre, gen):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = None
        self.__stats = None
        self.__generacion = gen


    def get_nombre(self):
        return self.__nombre


    def get_id(self):
        return self.__id


    def get_generacion(self):
        return self.__generacion


    def set_tipo(self, tipo):
        self.__tipo = tipo


    def get_tipo(self):
        return self.__tipo


    def set_stats(self, stats):
        self.__stats = stats


    def get_stats(self):
        return self.__stats

