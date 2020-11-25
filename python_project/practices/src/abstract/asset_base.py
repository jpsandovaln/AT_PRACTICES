from abc import ABC, abstractmethod


class AssetBase(ABC):
    @abstractmethod
    def get_value(self):
        pass

    def show_message(self):
        print('Hello')

