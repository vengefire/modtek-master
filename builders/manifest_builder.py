from builders.base_builder import BaseBuilder
from builders.manifest_entry_builder import ManifestEntryBuilder


class ManifestBuilder(BaseBuilder):
    @staticmethod
    def build_manifest(mod):
        manifest_json = mod.json['Manifest'] if 'Manifest' in mod.json else None

        if manifest_json is None:
            return

        for entry_json in manifest_json:
            entry = ManifestEntryBuilder.build_from_json(entry_json, mod)
            ManifestEntryBuilder.expand_manifest_entry(entry)
            mod.manifest_entries.append(entry)
