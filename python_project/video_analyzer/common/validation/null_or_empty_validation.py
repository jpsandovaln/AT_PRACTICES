from common.validation.validation_strategy import ValidationStrategy
from common.exception.validate_error import ValidateError


class NullOrEmptyValidation(ValidationStrategy):
    def __init__(self, value):
        self.__value = value

    def validate(self):
        if self.__value is None or not self.__value:
            raise ValidateError('Data is none or empty')
