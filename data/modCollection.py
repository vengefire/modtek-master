import os
from os.path import isdir, join, isfile

from data.mod import Mod
from util.logging import Logging


class ModCollection:
    _logger = Logging.get_default_logger()

    def __init__(self, path):
        self.path = path
        self.__mods = []
        self.__invalidMods = []
        self.__modLoadOrder = []

    @property
    def path(self):
        return self.__path

    @property
    def mods(self):
        return self.__mods

    @property
    def invalid_mods(self):
        return self.__invalidMods

    @property
    def mod_load_order(self):
        return self.__modLoadOrder

    @path.setter
    def path(self, path):
        self.__path = path

    @staticmethod
    def build_from_path(path):
        ModCollection._logger.info(f'Building mod collection from path [{path}]')
        mod_collection = ModCollection(path)
        mod_collection.parse_mods()
        mod_collection.validate_mods()
        return mod_collection

    def parse_mods(self):
        mod_package_paths = filter(lambda d: isdir(join(self.path, d)) and isfile(join(self.path, d, 'mod.json')), os.listdir(self.path))
        for mod_package_path in mod_package_paths:
            self.mods.append(Mod.build_from_definition(join(self.path, mod_package_path)))

    @staticmethod
    def validate_mod_configuration(mod):
        return mod.enabled

    def validate_mod_dependencies(self, mod):
        missing_dependencies = [dependency for dependency in mod.depends_on if dependency not in [mod.name for mod in self.mods if mod.name == dependency]]
        invalid_dependencies = [dependency for dependency in [mod for mod in mod.depends_on if mod not in missing_dependencies] if
                                dependency not in [mod.name for mod in self.mods if mod.name == dependency and self.validate_mod_configuration(mod) and self.validate_mod_dependencies(mod)]]
        return missing_dependencies, invalid_dependencies

    def validate_mods(self):
        for mod in self.mods:
            missing_dependencies, invalid_dependencies = self.validate_mod_dependencies(mod)
            self.invalid_mods.append((mod, f'Missing dependencies - {missing_dependencies}, invalid dependencies = {invalid_dependencies}')) if len(missing_dependencies) > 0 or len(invalid_dependencies) > 0 else None
