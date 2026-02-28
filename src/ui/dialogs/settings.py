from PySide6.QtWidgets import QWidget

from modorganizer.ui.qt.settingsdialog_ui import Ui_SettingsDialog


class SettingsDialog(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
