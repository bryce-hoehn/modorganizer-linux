from pathlib import Path
from typing import Dict, Optional
import json


class SteamClient:
    def get_steam_path(self):
        """Get Steam installation directory on Linux."""
        steam_path = Path.home() / ".steam" / "steam"
        if steam_path.exists():
            return steam_path
        # Flatpak Steam
        flatpak_path = (
            Path.home()
            / ".var"
            / "app"
            / "com.valvesoftware.Steam"
            / ".steam"
            / "steam"
        )
        if flatpak_path.exists():
            return flatpak_path
        return None

    def get_installed_games(self) -> Dict[str, Path]:
        """Get dictionary of installed Steam games.

        Returns:
            Dictionary mapping Steam App IDs to game paths
        """
        steam_path = self.get_steam_path()
        if not steam_path:
            return {}

        steamapps = steam_path / "steamapps"
        if not steamapps.exists():
            return {}

        games = {}
        # Parse appmanifest_*.acf files
        for manifest in steamapps.glob("appmanifest_*.acf"):
            data = self.parse_acf(manifest)
            if "AppState" in data:
                app_state = data["AppState"]
                appid = app_state.get("appid", "")
                installdir = app_state.get("installdir", "")
                if appid and installdir:
                    games[appid] = steamapps / "common" / installdir
        return games

    def get_supported_games(self):
        """Get list of supported and detected games.

        Args:
            game_manager: Optional game plugin manager instance

        Returns:
            List of dictionaries containing game information
        """

        steam_games = self.get_installed_games()
        return steam_games

    def parse_acf(self, path):
        """Parse Steam ACF file format."""
        content = path.read_text()
        lines = content.splitlines()
        result = []

        for index, line in enumerate(lines):
            line = line.strip().replace("\t\t", ":")

            if index == 0:
                continue

            if line == "{" or line == "}":
                result.append(line)
                continue

            try:
                key, val = line.split(":", 1)
                result.append(f"{key}:{val},")
            except ValueError:
                result.append(f"{line}:")

        json_data = "".join(result)

        json_data = json_data.replace(",}", "}")

        json_data = json_data.replace('}"', '},"')

        data = json.loads(json_data)

        return data
