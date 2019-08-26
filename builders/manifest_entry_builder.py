from os import walk

from builders.base_builder import BaseBuilder
from data.enums import ModTekInstructionObjects
from data.manifestEntry import ManifestEntry
from factories.object_builder_factory import ObjectBuilderFactory


class ManifestEntryBuilder(BaseBuilder):
    @staticmethod
    def build_from_json(entry_json, mod):
        entry = ManifestEntry(entry_json['Type'], mod.path, entry_json['Path'], entry_json['AddToDB'] if 'AddToDB' in entry_json else False)
        return entry

    @staticmethod
    def expand_manifest_entry(manifest_entry):
        if manifest_entry.object_type in ModTekInstructionObjects:
            pass
        object_builder = ObjectBuilderFactory.build_from_type(manifest_entry.object_type)
        root, directories, files = list(walk(manifest_entry.full_path))[0]
        for file in files:
            BaseBuilder._logger.debug(f'Processing {file}')
            # game_object = object_builder.build_object_from_definition()
