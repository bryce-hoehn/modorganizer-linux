from PySide6.QtWidgets import QWidget

from modorganizer.ui.qt.profilesdialog import Ui_ProfilesDialog


class ProfileManager(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ProfilesDialog()
        self.ui.setupUi(self)
