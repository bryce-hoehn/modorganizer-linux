import sys
import json
from core.main_window import MainWindow
from PySide6.QtWidgets import QApplication
from ui.dialogs.instance_wizard import InstanceWizard
from modorganizer import DATA_DIR, CONFIG_DIR


def main():
    if not DATA_DIR.is_dir():
        DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not CONFIG_DIR.is_dir():
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    app = QApplication(sys.argv)

    instances = []

    for instance in DATA_DIR.iterdir():
        if (instance / "instance.json").exists():
            with open(instance / "instance.json") as f:
                data = json.load(f)
                instances.append(data)

    if instances:
        # instance(s) exist, show instance selection dialog
        window = MainWindow()
        window.show()
    else:
        # instance wizard
        window = InstanceWizard()
        window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
