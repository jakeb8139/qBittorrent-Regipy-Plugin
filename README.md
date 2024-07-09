# qBittorrent-Regipy-Plugin
A plugin for Regipy to pull qBittorrent keys/values from the registry. Checks for installation path, and remnants.

Thank you to the folks working on Regipy for creating such a seemless and easy to work with library.


To install:

  1. Add the qbittorrent.py to the plugins/software folder of regipy.
  2. Initialize the plugin by adding "from .software.qbittorrent import QbittorentPlugin" to the __init__.py file in regipy/plugins
