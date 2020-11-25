from src.exception.invalid_data_error import InvalidDataError


class UnitTestExample:
    def sum_list(self, list):
        try:
            print(len(list))
            result = 0
            for element in list:
                result += element
        except TypeError:
            raise InvalidDataError()
        return result

    def is_adult(self, name, age):
        if age > 18:
            return '{} is adult with {} years old'.format(name, age)
        else:
            raise InvalidDataError('{} is not adult with {} years old'.format(name, age))
