from os.path import splitext
from pathlib import Path

from builders.object_builders.object_builder import ObjectBuilder
from data.gameObject import GameObject


class PrefabObjectBuilder(ObjectBuilder):
    def __init__(self, manifest_entry):
        super().__init__(manifest_entry)

    def build_objects(self):
        part_path = Path(self.manifest_entry.full_path).name
        part_name = splitext(part_path)[0]
        self._logger.debug(f'Processed prefab [{part_name}]')
        return GameObject(self.manifest_entry.object_type, part_name, part_name, self.manifest_entry.full_path)
