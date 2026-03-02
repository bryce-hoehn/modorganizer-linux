import json
import os
import threading
from PySide6.QtCore import QUrl, Signal, QObject
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLineEdit
from typing import Optional
from modorganizer.utils.nexus_sso import NexusSSO


from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
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
from modorganizer.utils.steam_utils import SteamClient
from modorganizer import DATA_DIR, CONFIG_DIR
from modorganizer.plugins.games.game_manager import GameManager
from modorganizer.utils.nexus_sso import NexusSSO


class InstanceWizard(QWizard):
    def __init__(self):
        super().__init__()

        # Initialize game manager and load all plugins
        self.game_manager = GameManager()
        self.game_plugins = self.game_manager.load_all_plugins()

        self.addPage(IntroPage())
        self.addPage(GamePage(self))
        self.addPage(GameEditionPage(self))
        self.addPage(NameInstancePage(self))
        self.addPage(NexusPage(self))
        self.addPage(ConfirmationPage(self))

    def get_game_names(self):
        """Get a list of game names from loaded plugins."""
        names = []
        for slug, plugin_class in self.game_plugins.items():
            # Create a temporary instance to get the game name
            plugin = plugin_class()
            if hasattr(plugin, "gameName"):
                names.append(plugin.gameName())
            elif hasattr(plugin, "Name"):
                names.append(plugin.Name)
        return names

    def accept(self):
        """Called when user clicks Finish"""
        # Access all registered fields
        selected_game = self.field("selectedGame")
        selected_edition = self.field("selectedEdition")
        instance_name = self.field("instanceName")

        print(f"Creating instance '{instance_name}' for {selected_game}")

        data = {
            "game": selected_game,
            "edition": selected_edition,
            "name": instance_name,
        }

        instance_dir = f"{DATA_DIR}/{instance_name}"

        os.makedirs(instance_dir, exist_ok=True)

        with open(f"{instance_dir}/instance.json", "w") as f:
            json.dump(data, f)

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
        for game in self.wizard.get_game_names():
            game_list.addItem(game)

        self.registerField("selectedGame", game_list)

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

        self.label = QLabel()
        self.label.setWordWrap(True)

        self.instance_name = QLineEdit()
        self.registerField("instanceName*", self.instance_name)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.instance_name)
        self.setLayout(layout)

    def initializePage(self):
        """Called when this page is about to be shown"""
        game_index = self.field("selectedGame")
        game_names = self.wizard.get_game_names()
        game_name = game_names[game_index]

        self.label.setText(
            f'<h3>Customize name for this <span style="white-space: nowrap;">{game_name}</span> instance.</h3>'
        )

        self.instance_name.setText(game_name)


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

        self.registerField("nexusApiKey", self, "_api_key", "api_key_received")

        h_layout = QHBoxLayout()

        self.connect_button = QPushButton()
        self.connect_button.setText("Connect to Nexus")
        self.connect_button.clicked.connect(self._on_connect_clicked)

        self.manual_connect_button = QPushButton()
        self.manual_connect_button.setText("Enter API Key Manually")
        self.manual_connect_button.clicked.connect(self._on_manual_key_clicked)

        h_layout.addWidget(self.connect_button)
        h_layout.addStretch()
        h_layout.addWidget(self.manual_connect_button)

        self.nexus_log = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(subtitle)
        layout.addWidget(label)
        layout.addLayout(h_layout)
        layout.addWidget(self.nexus_log)
        self.setLayout(layout)

        self._sso_client: Optional[NexusSSO] = None
        self._api_key: Optional[str] = None

    def _on_connect_clicked(self):
        """Handle SSO connect button click."""
        self.nexus_log.addItem("Connecting to Nexus SSO...")
        self.connect_button.setEnabled(False)

        self._sso_client = NexusSSO()

        # Connect signals - these are thread-safe in Qt
        self._sso_client.auth_url_received.connect(self._open_browser)
        self._sso_client.api_key_received.connect(self._on_api_key_received)
        self._sso_client.error_occurred.connect(self._on_sso_error)

        # Run in separate thread
        thread = threading.Thread(target=self._sso_client.connect, daemon=True)
        thread.start()

    def _open_browser(self, auth_url: str):
        """Called when auth URL is received."""
        self.nexus_log.addItem("Opening browser for authorization...")
        QDesktopServices.openUrl(QUrl(auth_url))
        self.nexus_log.addItem("Please authorize in your browser...")

    def _on_api_key_received(self, api_key: str):
        """Called when API key is received."""
        self._api_key = api_key
        self.nexus_log.addItem("✓ Successfully connected to Nexus!")
        self.wizard.setField("nexusApiKey", api_key)

    def _on_sso_error(self, error_msg: str):
        """Handle SSO connection errors."""
        self.nexus_log.addItem(f"✗ {error_msg}")
        self.connect_button.setEnabled(True)

    def _on_manual_key_clicked(self):
        """Handle manual API key entry."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Enter Nexus API Key")
        layout = QVBoxLayout()

        label = QLabel("Enter your Nexus API key:")
        input_field = QLineEdit()

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)

        layout.addWidget(label)
        layout.addWidget(input_field)
        layout.addWidget(button_box)
        dialog.setLayout(layout)

        if dialog.exec() == QDialog.Accepted:
            api_key = input_field.text().strip()
            if api_key:
                self._api_key = api_key
                self.wizard().setField("nexusApiKey", api_key)
                self.nexus_log.addItem(f"✓ API key set manually: {api_key[:20]}...")
            else:
                self.nexus_log.addItem("✗ No API key entered")

    def cleanupPage(self):
        """Called when leaving the page."""
        if self._sso_client:
            self._sso_client.disconnect()


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
        launch_button.setText("Launch new instance")

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

        edition_index = self.wizard.field("selectedEdition")
        editions = ["Steam"]

        game_names = self.wizard.get_game_names()

        self.review.setText(
            f"""
            <b>Game:</b> {game_names[game_index]}<br>
            <b>Edition:</b> {editions[edition_index]}<br>
            <b>Instance Name:</b> {self.wizard.field("instanceName")}
        """
        )
