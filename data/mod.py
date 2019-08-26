from util.logging import Logging


class Mod:
    _logger = Logging.get_default_logger()

    def __init__(self, path, json_object):
        self.path = path
        self.__json = json_object
        self.__manifest_entries = []

    @property
    def path(self):
        return self.__path

    @property
    def name(self):
        return self.__json['Name']

    @property
    def enabled(self):
        return self.__json["Enabled"] if 'Enabled' in self.__json else True

    @property
    def dll(self):
        return self.__json["DLL"] if 'DLL' in self.__json else None

    @property
    def depends_on(self):
        return self.__json["DependsOn"] if 'DependsOn' in self.__json else []

    @property
    def optionally_depends_on(self):
        return self.__json["OptionallyDependsOn"] if 'OptionallyDependsOn' in self.__json else []

    @path.setter
    def path(self, path):
        self.__path = path

    @property
    def manifest_entries(self):
        return self.__manifest_entries

    @property
    def json(self):
        return self.__json

    def __repr__(self):
        return f'Mod [Name - {self.name}] | [Enabled - {self.enabled}]'
