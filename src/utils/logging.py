# log_handler.py
from PySide6.QtCore import QObject, Signal, QAbstractListModel, Qt

class ListViewLogger(QObject):
    message_written = Signal(str)

    def write(self, message):
        if message.strip():
            self.message_written.emit(message)

    def flush(self):
        pass

class LogModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.logs = []

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.logs[index.row()]
        return None

    def rowCount(self, parent=None):
        return len(self.logs)

    def add_log(self, message):
        self.beginInsertRows(self.index(len(self.logs), 0), len(self.logs), len(self.logs))
        self.logs.append(message)
        self.endInsertRows()
 
