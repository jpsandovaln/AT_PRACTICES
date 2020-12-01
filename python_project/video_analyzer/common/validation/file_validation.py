from common.validation.validation_strategy import ValidationStrategy
from common.exception.validate_error import ValidateError
import os


class FileValidation(ValidationStrategy):
    def __init__(self, value):
        self.__value = value

    def validate(self):
        if self.__value is None or not os.path.isfile(self.__value):
            raise ValidateError('Invalid File')
