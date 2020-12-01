from configparser import ConfigParser


class ConfigManager:
    __instance = None
    name = ''

    def __new__(cls, *args, **kwargs):
        if ConfigManager.__instance is None:
            ConfigManager.__instance = object.__new__(cls)
            ConfigManager.set_configuration(ConfigManager.__instance)
        return ConfigManager.__instance

    def set_configuration(self):
        self.config_object = ConfigParser()
        self.config_object.read('D:\\AT_PRATICES\\AT_PRACTICES\\python_project\\video_analyzer\\config\\config.properties')
        self.config_conversion = self.config_object['CONVERSION']

    def __init__(self):
        pass

    def get_value_as_string(self, key):
        return self.config_conversion[key]

    def get_value_as_list(self, key):
        value = self.get_value_as_string(key)
        list_value = list(value.split(','))
        return [item.strip() for item in list_value]

    def __str__(self):
        return self.name

