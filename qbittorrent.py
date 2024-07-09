import logging

from regipy.hive_types import SOFTWARE_HIVE_TYPE
from regipy.plugins.plugin import Plugin
from regipy.utils import get_subkey_values_from_list
from regipy.exceptions import RegistryKeyNotFoundException

'''
A regipy plugin to pull qBittorrent registry keys, find installation path, or find remnents of previous install.
Version: 20240708
Expected Hive: Software
Author: Jake Burch
Email: jakehburchiii@gmail.com
'''

logger = logging.getLogger(__name__)

# Designating the two paths. KEY_PATH is expected when qBittorrent has been installed, PERSISTANCE_PATH WHEN UNINSTALLED
KEY_PATH = r"\WOW6432Node\qBittorrent"
PERSISTANCE_PATH = r"\Classes\.torrent"


class QbittorentPlugin(Plugin):
    NAME = 'qBittorrent_plugin'
    DESCRIPTION = 'Plugin that extracts keys/values related to qBittorent'
    COMPATIBLE_HIVE = SOFTWARE_HIVE_TYPE

    # Determining which hive this plugin should be run for (HKLM/SOFTWARE)
    def can_run(self):
        # TODO: Choose the relevant condition - to determine if the plugin is relevant for the given hive
        return self.registry_hive.hive_type == SOFTWARE_HIVE_TYPE

    def run(self):
        # TODO: Return the relevant values
        logger.debug('Starting qBittorent Plugin...')

        # Try to find the install path, if not found, set install = None.
        try:
            install = self.registry_hive.get_key(KEY_PATH)

        except RegistryKeyNotFoundException as ex:
            install = None

        # Try to find the remnants path, if not found, set persist = None.
        try:
            persist = self.registry_hive.get_key(PERSISTANCE_PATH)

        except RegistryKeyNotFoundException:
            persist = None

        # If install is true (If the install exists in the registry), do...
        if install:
            try:
                if "qBittorrent" in install.get_value('InstallLocation'):

                    self.entries = {
                        'qBittorrent:': install.get_value('InstallLocation'),
                        'Installed:': True,
                    }

            except UnboundLocalError as ex:
                logger.debug(ex)

        # If install is not true (Install not in the registry), do...
        else:
            try:
                if "application/x-bittorrent" in persist.get_value('Content Type'):
                    self.entries = {
                        'Installed:': False,
                        'Remnants:': True,
                        'Location:': PERSISTANCE_PATH,
                        'Value:': persist.get_value('Content Type')
                    }
            # If install AND remnents are not found, Existance is set to zero in JSON.
            except UnboundLocalError as ex:
                    logger.debug(ex)
                    self.entries = {
                        'Existance:': None
                    }


