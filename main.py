import sys
import webbrowser
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QAbstractItemView, QWidget, QTreeWidgetItem
from PySide6.QtCore import QUrl, Qt
from ui.mainwindow import Ui_MainWindow
from ui.instancemanagerdialog import Ui_InstanceManagerDialog
from ui.profilesdialog import Ui_ProfilesDialog
from log_handler import ListViewLogger, LogModel
from utils.parse_config import ConfigHelper, get_executable_titles, get_mod_list

class InstanceManager(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_InstanceManagerDialog()
        self.ui.setupUi(self)

class ProfileManager(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ProfilesDialog()
        self.ui.setupUi(self)
        
class MainWindow(QMainWindow):
    def __init__(self, url=None):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # downloads
        self.ui.downloadView.setHeaderLabels(["Name", "Status", "Size", "Filename"])
        self.ui.downloadView.setAlternatingRowColors(True)
        QTreeWidgetItem(self.ui.downloadView, ["mod1.zip", "Installed", "5mb", "mod1.zip"])

        # modList
        modList = get_mod_list()
        self.ui.modList.setHeaderLabels(['Mod Name', 'Conflicts', 'Flags', 'Category', 'Version', 'Priority'])
        self.ui.modList.setAlternatingRowColors(True)

        for mod in modList:
            QTreeWidgetItem(self.ui.modList, [mod, '', '', '', '1', '1']).setCheckState(0, Qt.CheckState.Unchecked)

        # instance manager
        self.ui.actionChange_Game.triggered.connect(self.show_instance_manager)

        # nexus
        self.ui.actionNexus.triggered.connect(self.nexus)

        # profiles
        self.ui.actionAdd_Profile.triggered.connect(self.profile_manager)

        helper = ConfigHelper()

        current_profile = helper.get("General", "selected_profile")

        self.ui.profileBox.addItem(current_profile)
        # filter
        self.ui.displayCategoriesBtn.toggled.connect(self.filter_toggle)
        self.ui.categoriesGroup.setVisible(False)

        # buttons
        self.ui.actionInstallMod.triggered.connect(self.install_mod)
        self.ui.action_Refresh.triggered.connect(self.action_Refresh)
        self.ui.startButton.clicked.connect(self.startButton)

        # Setup the log list view
        self.log_model = LogModel(self)
        self.ui.logList.setModel(self.log_model)
        self.logger = ListViewLogger()
        self.logger.message_written.connect(self.log_model.add_log)

        # executables
        exes = get_executable_titles()
        self.ui.executablesListBox.addItems(exes)

        # Redirect stdout and stderr
        sys.stdout = self.logger
        sys.stderr = self.logger

        if url:
            self.handle_nxm_url(url)

    def action_Refresh(self):
        # Add your refresh functionality here
        print("Refresh button clicked")

    def filter_toggle(self, state):
        self.ui.categoriesGroup.setVisible(state)

    def show_instance_manager(self):
        self.w = InstanceManager()
        self.w.show()

    def startButton(self):
        # Add your launch functionality here
        print("Launch button clicked")
    
    def install_mod(self):
        dialog = QFileDialog(self)
        dialog.setDirectory('~/Downloads')
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setNameFilter("*.zip")
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                self.file_list.addItems([str(Path(filename)) for filename in filenames])
    
    def nexus(self):
        webbrowser.open("https://www.nexusmods.com/fallout4")

    def profile_manager(self):
        self.w = ProfileManager()
        self.w.show()

    def handle_nxm_url(self, url):
        # Parse the URL and handle it
        nxm_url = QUrl(url)
        if nxm_url.scheme() == "nxm":
            print(f"Handling NXM URL: {url}")
        else:
            print(f"Invalid URL: {url}")

if __name__ == "__main__":
    app = QApplication([])

    # Check if the application was started with a URL argument
    url = None
    if len(sys.argv) > 1:
        url = sys.argv[1]

    window = MainWindow(url)
    window.show()

    with open('ui/stylesheets/vs15 Dark.qss', 'r') as f:
        style = f.read()

        # Set the stylesheet of the application
        app.setStyleSheet(style)

    app.exec()
