from os import listdir

from builders.object_builders.object_builder import ObjectBuilder
from data.gameObject import GameObject


class AssetBundleObjectBuilder(ObjectBuilder):
    def __init__(self, manifest_entry):
        super().__init__(manifest_entry)

    def build_objects(self):
        for filename in listdir(self.manifest_entry.full_path):
            identifier = filename
            self._logger.debug(f'Processing Asset Bundle [{identifier}]')
            return GameObject(self.object_type, identifier, identifier, None)
