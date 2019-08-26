from argparse import ArgumentParser

from builders.mod_collection_builder import ModCollectionBuilder
from features.devUtils import generate_object_type_enum
from util.logging import Logging

if __name__ == '__main__':
    Logging.init_logging('./res/config.ini')
    logger = Logging.get_default_logger()
    try:
        parser = ArgumentParser(description='Utility for BattleTech ModTek mods.')
        parser.add_argument('btpath', metavar='"Battle Tech path"', type=str, help='HBS BattleTech folder')
        parser.add_argument('modspath', metavar='"ModTek mods path"', type=str, help='ModTek Mods folder')
        parser.add_argument('-ot', help='Enumerate distinct object types in the mod collection', action='store_true', default=False, dest='list_object_types')
        parser.add_argument('-v', help='Validate the mod collection', action='store_true', default=False, dest='validate_mods')

        args = parser.parse_args()

        logger.info('Starting up modtek-master bootstrapper...')

        mod_collection_path = args.modspath
        mod_collection = ModCollectionBuilder.build_from_path(mod_collection_path)
        logger.info(f'Loaded {len(mod_collection.mods)} mods : valid = [{len(mod_collection.valid_mods)}], invalid = [{len(mod_collection.invalid_mods)}]')

        if mod_collection.is_valid is not True:
            invalid_mods = '\r\n'.join(f'{invalid_mod[0]}\r\n{invalid_mod[1]}' for invalid_mod in mod_collection.invalid_mods)
            logger.warning(f'ModCollection is invalid. Please find invalid mods below:\r\n{invalid_mods}')

        if args.list_object_types:
            code = generate_object_type_enum(mod_collection)
            logger.info(f'--GEN : OBJECT TYPE ENUM CODE--\r\n{code}')

    except Exception:
        logger.exception(f'Error executing {__name__}')
