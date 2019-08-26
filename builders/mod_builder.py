import os

from builders.base_builder import BaseBuilder
from builders.manifest_builder import ManifestBuilder
from data.mod import Mod
from util.json import load_json_from_file


class ModBuilder(BaseBuilder):

    @staticmethod
    def build_from_definition(path):
        mod_config_path = os.path.join(path, 'mod.json')
        BaseBuilder._logger.debug(f'Parsing mod package config [{mod_config_path}]...')
        mod_definition = load_json_from_file(mod_config_path)
        new_mod = Mod(path, mod_definition)
        ManifestBuilder.build_manifest(new_mod)
        return new_mod
