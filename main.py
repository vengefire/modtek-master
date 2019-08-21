from data.modCollection import ModCollection

if __name__ == '__main__':
    mod_collection_path = r'D:\XLRP Fixes\XLRP - Reference - 20190725 - With CAB'
    print('Starting up modtek-master boot strapper...')
    mod_collection = ModCollection.build_from_path(mod_collection_path)
    [print(mod) for mod in mod_collection.mods]
