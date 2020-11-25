class Animal:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def get_name(self):
        return self.__name

    def set_name__(self, name):
        self.__name = name

    #def desplazar(self):
    #    pass
