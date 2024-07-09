# qBittorrent-Regipy-Plugin
A plugin for Regipy to pull qBittorrent keys/values from the registry. Checks for installation path, and remnants.

This was created for DFOR-673: Windows Registry Forensics. The assignment required to find a program with significant forensic value that did not fully clean itself out of the registry upon uninstalling. The plugin had to detect whether qBittorrent was installed, never installed, or installed at one point.

Thank you to the folks working on Regipy for creating such a seemless and easy to work with library.


To install:

  1. Add the qbittorrent.py to the plugins/software folder of regipy.
  2. Initialize the plugin by adding "from .software.qbittorrent import QbittorentPlugin" to the __init__.py file in regipy/plugins
