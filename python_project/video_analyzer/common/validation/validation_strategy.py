from abc import ABC, abstractmethod


class ValidationStrategy:
    @abstractmethod
    def validate(self):
        pass
