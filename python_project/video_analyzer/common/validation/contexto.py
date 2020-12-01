class Context:
    def __init__(self, validation_strategies):
        self.__validation_strategies = validation_strategies

    def validate(self):
        for strategy in self.__validation_strategies:
            strategy.validate()
