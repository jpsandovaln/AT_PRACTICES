from src.heritage.animal import Animal


class Acuatico(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def desplazar(self):
        print('nadando....')

