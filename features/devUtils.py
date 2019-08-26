def extract_distinct_object_type_strings(mod_collection):
    distinct_set = set()
    [distinct_set.add(entry.object_type_string) for mod in mod_collection.mods for entry in mod.manifest_entries]
    return distinct_set


def generate_object_type_enum(mod_collection):
    distinct_object_type_strings = sorted(extract_distinct_object_type_strings(mod_collection))

    code = 'from enum import Enum\r\n\r\n' + \
           'class ObjectType(Enum):\r\n' + \
           '\r\n'.join([f"\t{object_type} = '{object_type}'" for object_type in distinct_object_type_strings]) + \
           '\r\n'
    return code.replace('\t', '    ')
