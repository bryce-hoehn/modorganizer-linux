from PySide6.QtWidgets import QWidget

from ui.generated.instancemanagerdialog import Ui_InstanceManagerDialog


class InstanceManager(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_InstanceManagerDialog()
        self.ui.setupUi(self)
