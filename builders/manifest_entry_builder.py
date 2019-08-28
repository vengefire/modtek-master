from builders.base_builder import BaseBuilder
from data.enums import ModTekInstructionObjects
from data.manifestEntry import ManifestEntry
from factories.object_builder_factory import ObjectBuilderFactory


class ManifestEntryBuilder(BaseBuilder):
    @staticmethod
    def build_from_json(entry_json, mod):
        entry = ManifestEntry(entry_json['Type'], mod.path, entry_json['Path'], entry_json['AddToDB'] if 'AddToDB' in entry_json else False, entry_json['AssetBundleName'] if 'AssetBundleName' in entry_json else None)
        return entry

    @staticmethod
    def expand_manifest_entry(manifest_entry):
        if manifest_entry.object_type in ModTekInstructionObjects:
            pass
        object_builder = ObjectBuilderFactory.build_from_type(manifest_entry)
        objects = object_builder.build_objects()
