from src.heritage.animal import Animal


class Volador(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def desplazar(self):
        print("volando......")
