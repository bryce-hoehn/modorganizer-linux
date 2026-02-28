from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
    QRadioButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
    QWizard,
    QWizardPage,
    QCheckBox,
)
from utils.steam_utils import SteamClient


class InstanceWizard(QWizard):
    def __init__(self):
        super().__init__()

        self.game_names = [
            "Skyrim",
            "Skyrim Special Edition",
            "Fallout 4",
            "Cyberpunk 2077",
        ]

        self.addPage(IntroPage())
        self.addPage(GamePage(self))
        self.addPage(GameEditionPage(self))
        self.addPage(NameInstancePage(self))
        self.addPage(NexusPage(self))
        self.addPage(ConfirmationPage(self))

    def accept(self):
        """Called when user clicks Finish"""
        # Access all registered fields
        selected_game = self.field("selectedGame")
        selected_edition = self.field("selectedEdition")
        instance_name = self.field("instanceName")

        print(f"Creating instance '{instance_name}' for {selected_game}")

        # Do your actual work here (create instance, etc.)

        # Call parent accept to close the wizard
        super().accept()


class IntroPage(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Creating a new instance")
        label = QLabel(
            """
            <h3>What is an instance?</h3>\n
            <p>An instance is a full set of mods, downloads, profiles and configuration for a game. Each game must be managed in its own instance. Mod Organizer can freely switch between instances.</p>
        """
        )
        label.setWordWrap(True)
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)


class GamePage(QWizardPage):
    def __init__(self, wizard):
        super().__init__()
        self.wizard = wizard
        self.setTitle("Creating a new instance")
        label = QLabel("<h3>Select the game to manage.</h3>")

        game_list = QListWidget()
        for game in self.wizard.game_names:
            game_list.addItem(game)

        self.registerField("selectedGame*", game_list)

        h_layout = QHBoxLayout()

        show_all_button = QCheckBox()
        show_all_button.setText("Show all supported games")

        game_filter = QLineEdit()

        h_layout.addWidget(show_all_button)
        h_layout.addStretch()
        h_layout.addWidget(game_filter)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(game_list)
        layout.addLayout(h_layout)
        self.setLayout(layout)


class GameEditionPage(QWizardPage):
    def __init__(self, wizard):
        super().__init__()
        self.wizard = wizard
        self.setTitle("Creating a new instance")
        subtitle = QLabel("<h3>Select the game edition.</h3>")
        label = QLabel(
            "This game has multiple variants. The correct one must be selected or Mod Organizer will not be able to launch the game properly. Currently only Steam is supported."
        )
        label.setWordWrap(True)

        edition_list = QListWidget()
        edition_list.addItem("Steam")

        self.registerField("selectedEdition*", edition_list)

        layout = QVBoxLayout()
        layout.addWidget(subtitle)
        layout.addWidget(label)
        layout.addWidget(edition_list)
        self.setLayout(layout)


class NameInstancePage(QWizardPage):
    def __init__(self, wizard):
        super().__init__()
        self.wizard = wizard
        self.setTitle("Creating a new instance")
        label = QLabel(
            '<h3>Customize the name for this <span style="white-space: nowrap;">%1</span> instance.</h3>'
        )
        label.setWordWrap(True)

        instance_name = QLineEdit()

        self.registerField("instanceName*", instance_name)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(instance_name)
        self.setLayout(layout)


class NexusPage(QWizardPage):
    def __init__(self, wizard):
        super().__init__()
        self.wizard = wizard
        self.setTitle("Creating a new instance")
        subtitle = QLabel("<h3>Link Mod Organizer with your Nexus account</h3>")
        label = QLabel(
            "Linking with Nexus allows you to download mods directly from Mod Organizer and automatically check for updates. This is optional."
        )
        label.setWordWrap(True)

        h_layout = QHBoxLayout()

        connect_button = QPushButton()
        connect_button.setText("Connect to Nexus")

        manual_connect_button = QPushButton()
        manual_connect_button.setText("Enter API Key Manually")

        h_layout.addWidget(connect_button)
        h_layout.addStretch()
        h_layout.addWidget(manual_connect_button)

        nexus_log = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(subtitle)
        layout.addWidget(label)
        layout.addLayout(h_layout)
        layout.addWidget(nexus_log)

        self.setLayout(layout)


class ConfirmationPage(QWizardPage):
    def __init__(self, wizard):
        super().__init__()
        self.wizard = wizard
        self.setTitle("Creating a new instance")

        subtitle = QLabel("<h3>Confirmation</h3>")
        label = QLabel(
            "The instance is about to be created. Review the information below and press 'Finish'."
        )
        label.setWordWrap(True)

        self.review = QLabel()

        launch_button = QCheckBox()
        launch_button.setText("Launch the new instance")

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(launch_button)

        layout = QVBoxLayout()
        layout.addWidget(subtitle)
        layout.addWidget(label)
        layout.addWidget(self.review)
        layout.addStretch()
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def initializePage(self):
        """Called when this page is about to be shown"""
        game_index = self.wizard.field("selectedGame")

        # Handle the edition index (it's also a QListWidget returning int)
        edition_index = self.wizard.field("selectedEdition")
        editions = ["Steam"]

        self.review.setText(
            f"""
            <b>Game:</b> {self.wizard.game_names[game_index]}<br>
            <b>Edition:</b> {editions[edition_index]}<br>
            <b>Instance Name:</b> {self.wizard.field("instanceName")}
        """
        )
