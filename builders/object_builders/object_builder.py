from builders.base_builder import BaseBuilder


class ObjectBuilder(BaseBuilder):
    def __init__(self, manifest_entry):
        self.__object_definition = None
        self.__filename = None
        self.__file_extension = None
        self.__manifest_entry = manifest_entry

    @property
    def file_extension(self):
        return self.__file_extension

    @property
    def object_definition(self):
        return self.__object_definition

    @property
    def object_type(self):
        return self.__manifest_entry.object_type

    @property
    def file_name(self):
        return self.__filename

    @property
    def manifest_entry(self):
        return self.__manifest_entry

    def build_objects(self):
        raise NotImplementedError
