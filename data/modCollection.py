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
    def valid_mods(self):
        return [mod for mod in self.mods if mod.name not in map(lambda d: d[0].name, self.invalid_mods)]

    @property
    def mod_load_order(self):
        return self.__modLoadOrder

    @path.setter
    def path(self, path):
        self.__path = path

    @property
    def is_valid(self):
        return len(self.invalid_mods) == 0

    @staticmethod
    def build_from_path(path):
        ModCollection._logger.info(f'Building mod collection from path [{path}]')
        mod_collection = ModCollection(path)
        mod_collection.parse_mods()
        mod_collection.validate_mods()
        mod_collection.build_load_order()
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
        invalid_dependencies = [dependency for dependency in [mod_name for mod_name in mod.depends_on if mod_name not in missing_dependencies] if
                                dependency not in [dependency_mod.name for dependency_mod in self.mods if
                                                   dependency_mod.name == dependency and self.validate_mod_configuration(dependency_mod) and self.validate_mod_dependencies(dependency_mod)[2] is True]]
        return missing_dependencies, invalid_dependencies, False if len(missing_dependencies) > 0 or len(invalid_dependencies) > 0 else True

    def validate_mods(self):
        for mod in self.mods:
            missing_dependencies, invalid_dependencies, result = self.validate_mod_dependencies(mod)
            self.invalid_mods.append((mod, f'Missing dependencies - {missing_dependencies}, invalid dependencies = {invalid_dependencies}')) if result is False else None

    def build_load_order(self):
        iteration = 1
        mods_to_load = self.valid_mods
        [self.mod_load_order.append(mod) for mod in mods_to_load if len(mod.depends_on) == 0 and len(mod.optionally_depends_on) == 0]
        [mods_to_load.remove(mod) for mod in self.mod_load_order]
        self._logger.info(f'\r\n--Load Order Round {iteration}--\r\n' + '\r\n'.join(map(lambda mod: mod.name, self.mod_load_order)))

        while len(mods_to_load) > 0:
            iteration += 1
            valid_dependent_mods = [mod for mod
                                    in mods_to_load
                                    if len([dependency for dependency in mod.depends_on
                                            if dependency not in map(lambda mod: mod.name, self.mod_load_order)]
                                           ) == 0
                                    and len([optional_dependency for optional_dependency in mod.optionally_depends_on
                                             if optional_dependency in map(lambda mod: mod.name, self.valid_mods) and optional_dependency not in map(lambda mod: mod.name, self.mod_load_order)]) == 0]
            [self.mod_load_order.append(mod) for mod in valid_dependent_mods]
            [mods_to_load.remove(mod) for mod in valid_dependent_mods]
            self._logger.info(f'\r\n--Load Order Round {iteration}--\r\n' + '\r\n'.join(map(lambda mod: mod.name, valid_dependent_mods)))
