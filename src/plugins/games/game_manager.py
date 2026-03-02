import pkgutil
import importlib
import inspect
import src.plugins.games as games_package
from modorganizer.plugins.utils.basic_game import BasicGame


class GameManager:
    def __init__(self):
        super().__init__()

    def load_all_plugins(self):
        plugins = {}

        for importer, module_name, ispkg in pkgutil.iter_modules(
            games_package.__path__
        ):
            if ispkg:  # Only load subpackages (directories with __init__.py)
                # Import the main module file (e.g., falloutnv.falloutnv)
                full_module_name = f"src.plugins.games.{module_name}.{module_name}"
                module = importlib.import_module(full_module_name)

                # Find the game plugin class (inherits from BasicGame)
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if (
                        issubclass(obj, BasicGame)
                        and obj is not BasicGame
                        and obj.__module__ == module.__name__
                    ):

                        # Use GameShortName as the key, fallback to module name
                        slug = getattr(obj, "GameShortName", module_name)
                        plugins[slug] = obj

        return plugins
