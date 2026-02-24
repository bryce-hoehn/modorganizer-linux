from PySide6.QtWidgets import QWidget

from ui.generated.profilesdialog import Ui_ProfilesDialog


class ProfileManager(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ProfilesDialog()
        self.ui.setupUi(self)
