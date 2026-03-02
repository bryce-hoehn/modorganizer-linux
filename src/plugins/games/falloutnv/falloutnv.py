from PySide6.QtCore import QFileInfo

import mobase

from modorganizer.plugins.utils.basic_game import BasicGame


class FalloutNVGame(BasicGame):
    Name = "Fallout New Vegas Plugin"
    Author = "Bryce Hoehn"
    Version = "0.1.0"
    GameName = "Fallout: New Vegas"
    GameShortName = "falloutnv"
    GameNexusName = "newvegas"
    GameValidShortNames = ["fnv"]
    GameLauncher = "FalloutNVLauncher.exe"
    GameBinary = "FalloutNV.exe"
    GameDataPath = ""
    GameDocumentDirectory = "%USERPROFILE%/Documents/My Games/FalloutNV"
    GameSavesDirectory = f"{GameDocumentDirectory}/Saves"
    GameSaveExtension = "fos"
    GameNexusId = 130
    GameSteamId = 22380

    def init(self, organizer: mobase.IOrganizer):
        super().init(organizer)
        return True

    def executables(self):
        return [
            mobase.ExecutableInfo(
                "New Vegas", QFileInfo(self.gameDirectory(), "FalloutNV.exe")
            ),
            mobase.ExecutableInfo(
                "Fallout Launcher",
                QFileInfo(self.gameDirectory(), "FalloutNVLauncher.exe"),
            ),
            mobase.ExecutableInfo(
                "NVSE",
                QFileInfo(self.gameDirectory(), "NVSE.exe"),
            ),
        ]

    def vanillaArchives(self):
        return (
            "Fallout - Textures.bsa",
            "Fallout - Textures2.bsa",
            "Fallout - Meshes.bsa",
            "Fallout - Voices1.bsa",
            "Fallout - Sound.bsa",
            "Fallout - Misc.bsa",
        )

    # ini_file = "fallout.ini"
