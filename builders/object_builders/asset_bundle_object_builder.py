from builders.object_builders.object_builder import ObjectBuilder
from data.gameObject import GameObject


class AssetBundleObjectBuilder(ObjectBuilder):
    def __init__(self, object_type, filename):
        super().__init__(object_type)
        self.__filename = filename

    def build_objects(self):
        identifier = self.__filename
        return GameObject(self.object_type, identifier, identifier, None)
