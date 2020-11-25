from src.heritage.animal import Animal
from src.heritage.acuatico import Acuatico
from src.heritage.Volador import  Volador
from src.heritage.anfibio import Anfibio
from src.abstract.asset_base import AssetBase
from src.abstract.asset_file import AssetFile
from src.calculate import Calculate
from src.unit_test.unit_test_example import UnitTestExample
from src.exception.invalid_data_error import InvalidDataError


if __name__ == '__main__':
    # animal = Animal('perro', 'blanco')
    '''animal2 = Volador('paloma', 'plomo')
    animal3 = Acuatico('Pejerrey', 'negro')
    animal4 = Anfibio('pato', 'blanco')

    animals = [animal2, animal3, animal4]

    for ani in animals:
        ani.desplazar()

    # asset = AssetBase()
    # asset.show_message()

    assetFile = AssetFile()
    assetFile.get_value()

    ab = AssetFile()
    cal = Calculate()
    print(cal.add_num(5, 8))'''
    try:
        test = UnitTestExample()
        print(test.sum_list([1, 2, 3]))
        print(test.sum_list([1, 2, 'hi']))
    except InvalidDataError as error:
        print(error)




