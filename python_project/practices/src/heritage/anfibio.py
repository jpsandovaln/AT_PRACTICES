from src.heritage.Volador import Volador
from src.heritage.acuatico import Acuatico


class Anfibio(Acuatico, Volador):
    def __init__(self, name, color):
        super().__init__(name, color)
