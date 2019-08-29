from os import listdir
from os.path import join, isdir
from os.path import splitext

from builders.object_builders.object_builder import ObjectBuilder
from util.json import load_json_from_file


class DefaultJsonObjectBuilder(ObjectBuilder):
    def __init__(self, object_type):
        super().__init__(object_type)

    def build_objects(self):
        if not isdir(self.manifest_entry.full_path):
            self._logger.warn(f'The specified manifest path [{self.manifest_entry.full_path}] does not exist.')
            return []

        files = [join(self.manifest_entry.full_path, filename) for filename in listdir(self.manifest_entry.full_path) if splitext(filename)[1] == '.json']
        objects = []
        for file in files:
            self._logger.debug(f'Processing [{file}]...')
            json = load_json_from_file(file)
            description = json['Description'] if 'Description' in json else None
            if description is not None:
                identifier = description['Id']
                name = description['Name']
                ui_name = description['UIName'] if 'UIName' in description else None
                icon = description['Icon'] if 'Icon' in description else None
            else:
                identifier = json['Id'] if 'Id' in json else json['ID'] if 'ID' in json else None
            self._logger.debug(f'Found Id [{identifier}]')

        return objects
