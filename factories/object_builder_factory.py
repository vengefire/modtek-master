from builders.object_builder import ObjectBuilder
from factories.base_factory import BaseFactory


class ObjectBuilderFactory(BaseFactory):
    @staticmethod
    def build_from_type(game_object_type):
        return ObjectBuilder(game_object_type)
