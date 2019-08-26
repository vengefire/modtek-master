from builders.base_builder import BaseBuilder
from data.gameObject import GameObject


class ObjectBuilder(BaseBuilder):
    def __init__(self, object_type):
        self.__object_type = object_type
        self.__object_definition = None
        self._filename = None

    def build_object_from_definition(self, object_definition, filename):
        description = object_definition['Description'] if 'Description' in object_definition else None
        if description is None:
            BaseBuilder._logger.warn(f'Object {object_definition} has no Description section.')
            return None

        id = description['Id']
        name = description['Name']
        ui_name = description['UIName']
        game_object = GameObject(self.__object_type, object_definition)
        return game_object
