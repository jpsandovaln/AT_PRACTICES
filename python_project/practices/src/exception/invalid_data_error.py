class InvalidDataError(Exception):
    def __init__(self, message = 'invalid data'):
        super().__init__(message)
