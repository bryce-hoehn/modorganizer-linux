class FalloutNVGame:
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

    vanilla_archives = (
        "Fallout - Textures.bsa",
        "Fallout - Textures2.bsa",
        "Fallout - Meshes.bsa",
        "Fallout - Voices1.bsa",
        "Fallout - Sound.bsa",
        "Fallout - Misc.bsa",
    )

    ini_file = "fallout.ini"

    def init(self, organizer: mobase.IOrganizer):
        super().init(organizer)
        self._register_feature(StardewValleyModDataChecker())
        return True

    def executables(self):
        return [
            mobase.ExecutableInfo(
                "SMAPI", QFileInfo(self.gameDirectory(), "StardewModdingAPI.exe")
            ),
            mobase.ExecutableInfo(
                "Stardew Valley", QFileInfo(self.gameDirectory(), "Stardew Valley.exe")
            ),
        ]
