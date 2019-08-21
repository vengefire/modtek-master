from argparse import ArgumentParser

from data.modCollection import ModCollection
from util.logging import Logging

if __name__ == '__main__':
    Logging.init_logging('./res/config.ini')
    logger = Logging.get_default_logger()
    try:
        parser = ArgumentParser(description='Utility for BattleTech ModTek mods.')
        parser.add_argument('btpath', metavar='"Battle Tech path"', type=str, help='HBS BattleTech folder')
        parser.add_argument('modspath', metavar='"ModTek mods path"', type=str, help='ModTek Mods folder')
        parser.add_argument('-v', help='Validate the mod collection', action='store_true', default=False, dest='validate_mods')

        args = parser.parse_args()

        mod_collection_path = args.modspath
        logger.info('Starting up modtek-master boot strapper...')
        mod_collection = ModCollection.build_from_path(mod_collection_path)
        [logger.info(mod) for mod in mod_collection.mods]
    except Exception:
        logger.exception(f'Error executing {__name__}')
