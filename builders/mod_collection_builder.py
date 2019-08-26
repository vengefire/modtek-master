from builders.base_builder import BaseBuilder
from data.modCollection import ModCollection


class ModCollectionBuilder(BaseBuilder):

    @staticmethod
    def build_from_path(path):
        BaseBuilder._logger.info(f'Building mod collection from path [{path}]')
        mod_collection = ModCollection(path)
        mod_collection.parse_mods()
        mod_collection.validate_mods()
        mod_collection.build_load_order()
        return mod_collection
