from pathlib import Path
from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QLabel,
    QMessageBox,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from modorganizer.ui.dialogs.instance_wizard import InstanceWizard
from modorganizer import DATA_DIR


class InstanceSelector(QDialog):
    """Dialog for selecting which instance to open on launch."""

    def __init__(self, instances: list[dict]):
        super().__init__()
        self.instances = instances
        self.selected_instance = None
        self._setup_ui()

    def _setup_ui(self):
        """Set up the user interface."""
        self.setWindowTitle("Select Instance")
        self.setMinimumWidth(500)
        self.setMinimumHeight(400)

        layout = QVBoxLayout()

        # Title label
        title_label = QLabel("Select an instance to open:")
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title_label.setFont(title_font)
        layout.addWidget(title_label)

        # Instance list
        self.instance_list = QListWidget()
        self._populate_instance_list()
        self.instance_list.itemDoubleClicked.connect(self._on_item_double_clicked)
        layout.addWidget(self.instance_list)

        # Button layout
        button_layout = QHBoxLayout()

        # New instance button
        self.new_button = QPushButton("New Instance")
        self.new_button.clicked.connect(self._on_new_instance)
        button_layout.addWidget(self.new_button)

        button_layout.addStretch()

        # Delete button
        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self._on_delete_instance)
        button_layout.addWidget(self.delete_button)

        # Cancel button
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.cancel_button)

        # Open button
        self.open_button = QPushButton("Open")
        self.open_button.clicked.connect(self._on_open_instance)
        self.open_button.setDefault(True)
        button_layout.addWidget(self.open_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        # Update button states based on selection
        self.instance_list.itemSelectionChanged.connect(self._update_button_states)
        self._update_button_states()

    def _populate_instance_list(self):
        """Populate the instance list with available instances."""
        self.instance_list.clear()

        for instance in self.instances:
            name = instance.get("name", "Unknown")
            game = instance.get("game", "Unknown")
            edition = instance.get("edition", "Unknown")

            # Create list item with formatted text
            item_text = (
                f"<b>{name}</b><br><span style='color: gray;'>{game} ({edition})</span>"
            )
            item = QListWidgetItem(item_text)
            item.setData(Qt.ItemDataRole.UserRole, instance)
            self.instance_list.addItem(item)

    def _update_button_states(self):
        """Update button states based on current selection."""
        has_selection = self.instance_list.currentItem() is not None
        self.open_button.setEnabled(has_selection)
        self.delete_button.setEnabled(has_selection)

    def _on_item_double_clicked(self, item: QListWidgetItem):
        """Handle double-click on an instance item."""
        self.selected_instance = item.data(Qt.ItemDataRole.UserRole)
        self.accept()

    def _on_new_instance(self):
        """Handle new instance button click."""
        wizard = InstanceWizard()
        if wizard.exec() == QDialog.DialogCode.Accepted:
            # Reload instances after creating new one
            self._reload_instances()

    def _on_delete_instance(self):
        """Handle delete instance button click."""
        current_item = self.instance_list.currentItem()
        if not current_item:
            return

        instance = current_item.data(Qt.ItemDataRole.UserRole)
        instance_name = instance.get("name", "this instance")

        # Confirm deletion
        reply = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete '{instance_name}'?\n\n"
            f"This will permanently delete all mods, saves, and settings for this instance.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            self._delete_instance(instance)

    def _delete_instance(self, instance: dict):
        """Delete an instance from disk."""
        instance_name = instance.get("name")
        instance_dir = DATA_DIR / instance_name

        try:
            # Delete the instance directory
            if instance_dir.exists():
                import shutil

                shutil.rmtree(instance_dir)

            # Remove from list and reload
            self._reload_instances()

            QMessageBox.information(
                self,
                "Instance Deleted",
                f"Instance '{instance_name}' has been deleted successfully.",
            )
        except Exception as e:
            QMessageBox.critical(
                self,
                "Deletion Failed",
                f"Failed to delete instance '{instance_name}':\n{str(e)}",
            )

    def _reload_instances(self):
        """Reload the list of instances from disk."""
        import json

        self.instances = []

        for instance_path in DATA_DIR.iterdir():
            if instance_path.is_dir() and (instance_path / "instance.json").exists():
                try:
                    with open(instance_path / "instance.json") as f:
                        data = json.load(f)
                        self.instances.append(data)
                except Exception as e:
                    print(f"Failed to load instance {instance_path.name}: {e}")

        self._populate_instance_list()

        # If no instances left, close dialog and show wizard
        if not self.instances:
            self.reject()

    def _on_open_instance(self):
        """Handle open instance button click."""
        current_item = self.instance_list.currentItem()
        if current_item:
            self.selected_instance = current_item.data(Qt.ItemDataRole.UserRole)
            self.accept()

    def get_selected_instance(self) -> dict | None:
        """Get the selected instance data."""
        return self.selected_instance
