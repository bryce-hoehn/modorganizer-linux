import sys
import webbrowser
from PySide6.QtWidgets import (
    QMainWindow,
    QTreeWidgetItem,
)
from PySide6.QtCore import QUrl, Qt
from modorganizer.ui.dialogs.instance_manager import InstanceManager
from modorganizer.ui.dialogs.profile import ProfileManager
from modorganizer.ui.dialogs.settings import SettingsDialog
from modorganizer.utils.logging import ListViewLogger, LogModel
from modorganizer.ui.qt.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, url=None):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # downloads
        self.ui.downloadView.setHeaderLabels(["Name", "Status", "Size", "Filename"])
        self.ui.downloadView.setAlternatingRowColors(True)
        QTreeWidgetItem(
            self.ui.downloadView, ["mod1.zip", "Installed", "5mb", "mod1.zip"]
        )

        # modList
        self.ui.modList.setHeaderLabels(
            ["Mod Name", "Conflicts", "Flags", "Category", "Version", "Priority"]
        )
        self.ui.modList.setAlternatingRowColors(True)

        # for mod in mod_list:
        #     QTreeWidgetItem(self.ui.modList, [mod, "", "", "", "1", "1"]).setCheckState(
        #         0, Qt.CheckState.Unchecked
        #     )

        # self.ui.activeModsCounter.display(len(mod_list))

        # instance manager
        self.ui.actionChange_Game.triggered.connect(self.show_instance_manager)

        # nexus
        self.ui.actionNexus.triggered.connect(self.nexus)

        # profiles
        self.ui.actionAdd_Profile.triggered.connect(self.profile_manager)

        # settings
        self.ui.actionSettings.triggered.connect(self.settings_dialog)

        # filter
        self.ui.displayCategoriesBtn.toggled.connect(self.filter_toggle)
        self.ui.categoriesGroup.setVisible(False)

        # buttons
        # self.ui.actionInstallMod.triggered.connect(self.install_mod)
        # self.ui.action_Refresh.triggered.connect(self.action_Refresh)
        self.ui.startButton.clicked.connect(self.startButton)

        # Setup the log list view
        self.log_model = LogModel(self)
        self.ui.logList.setModel(self.log_model)
        self.logger = ListViewLogger()
        self.logger.message_written.connect(self.log_model.add_log)

        # Redirect stdout and stderr
        sys.stdout = self.logger
        sys.stderr = self.logger

        if url:
            self.handle_nxm_url(url)

    def action_refresh(self):
        # Add your refresh functionality here
        print("Refresh button clicked")

    def filter_toggle(self, state):
        self.ui.categoriesGroup.setVisible(state)

    def show_instance_manager(self):
        self.w = InstanceManager()
        self.w.show()

    def startButton(self):
        print("Launch button clicked")

    def nexus(self):
        webbrowser.open("https://www.nexusmods.com/fallout4")

    def profile_manager(self):
        self.w = ProfileManager()
        self.w.show()

    def settings_dialog(self):
        self.w = SettingsDialog()
        self.w.show()

    def handle_nxm_url(self, url):
        # Parse the URL and handle it
        nxm_url = QUrl(url)
        if nxm_url.scheme() == "nxm":
            print(f"Handling NXM URL: {url}")
        else:
            print(f"Invalid URL: {url}")
