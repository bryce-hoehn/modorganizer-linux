"""Global configuration constants for Mod Organizer."""

from pathlib import Path
from xdg_base_dirs import xdg_data_home, xdg_config_home

# Contains instances and per-instance settings
DATA_DIR = xdg_data_home() / "mo2"

# Contains global MO2 settings
CONFIG_DIR = xdg_config_home() / "mo2"
