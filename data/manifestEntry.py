from os.path import join

from data.enums import ObjectType


class ManifestEntry:
    def __init__(self, object_type_string, base_path, manifest_path, add_to_db):
        self.__object_type_string = object_type_string
        self.__object_type = ObjectType(self.__object_type_string)
        self.__base_path = base_path
        self.__manifest_path = manifest_path
        self.__add_to_db = add_to_db
        self.__game_objects = []

    @property
    def object_type_string(self):
        return self.__object_type_string

    @property
    def object_type(self):
        return self.__object_type

    @property
    def game_objects(self):
        return self.__game_objects

    @property
    def full_path(self):
        return join(self.__base_path, self.__manifest_path)
