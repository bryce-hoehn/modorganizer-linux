import sys
import json
from pathlib import Path

from modorganizer.core.main_window import MainWindow
from PySide6.QtWidgets import QApplication, QDialog
from modorganizer.ui.dialogs.instance_selector import InstanceSelector
from modorganizer.ui.dialogs.instance_wizard import InstanceWizard
from modorganizer import DATA_DIR, CONFIG_DIR


def load_instances() -> list[dict]:
    """Load all instances from DATA_DIR."""
    instances = []

    if not DATA_DIR.is_dir():
        return instances

    for instance in DATA_DIR.iterdir():
        if instance.is_dir() and (instance / "instance.json").exists():
            try:
                with open(instance / "instance.json") as f:
                    data = json.load(f)
                    instances.append(data)
            except Exception as e:
                print(f"Failed to load instance {instance.name}: {e}")

    return instances


def main():
    if not DATA_DIR.is_dir():
        DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not CONFIG_DIR.is_dir():
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    app = QApplication(sys.argv)

    instances = load_instances()

    while True:
        selected_instance = None

        if instances:
            # Show instance selector
            selector = InstanceSelector(instances)
            if selector.exec() == QDialog.DialogCode.Accepted:
                selected_instance = selector.get_selected_instance()
            else:
                # User cancelled or deleted all instances
                instances = load_instances()
                if not instances:
                    # No instances left, show wizard
                    wizard = InstanceWizard()
                    if wizard.exec() == QDialog.DialogCode.Accepted:
                        instances = load_instances()
                        continue
                    else:
                        break
                continue
        else:
            # No instances, show wizard
            wizard = InstanceWizard()
            if wizard.exec() == QDialog.DialogCode.Accepted:
                instances = load_instances()
                continue
            else:
                break

        if selected_instance:
            # Open main window with selected instance
            window = MainWindow()
            window.setWindowTitle(f"Mod Organizer - {selected_instance['name']}")
            window.show()
            break

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
