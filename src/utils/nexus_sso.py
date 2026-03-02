import json
import uuid
import threading
import websocket
from typing import Optional
from PySide6.QtCore import Signal, QObject

APP_SLUG = "modorganizer2"
SSO_URL = "wss://sso.nexusmods.com"
AUTH_URL = "https://www.nexusmods.com/sso"


class NexusSSO(QObject):
    """SSO client with Qt signals for thread-safe communication."""

    auth_url_received = Signal(str)
    api_key_received = Signal(str)
    error_occurred = Signal(str)

    def __init__(self):
        super().__init__()
        self._uuid = str(uuid.uuid4())
        self._connection_token: Optional[str] = None
        self._api_key: Optional[str] = None
        self._ws: Optional[websocket.WebSocketApp] = None
        self._thread: Optional[threading.Thread] = None

    def connect(self) -> None:
        """Connect to SSO server."""

        def on_open(ws):
            """Called when connection opens."""
            data = {"id": self._uuid, "token": self._connection_token, "protocol": 2}
            ws.send(json.dumps(data))

        def on_message(ws, message):
            """Called when message received."""
            try:
                data = json.loads(message)
                if not data.get("success"):
                    error = data.get("error", "Unknown error")
                    self.error_occurred.emit(f"SSO error: {error}")
                    return

                payload = data.get("data", {})

                if "connection_token" in payload:
                    self._connection_token = payload["connection_token"]
                    auth_url = f"{AUTH_URL}?id={self._uuid}&application={APP_SLUG}"
                    self.auth_url_received.emit(auth_url)

                if "api_key" in payload:
                    self._api_key = payload["api_key"]
                    self.api_key_received.emit(self._api_key)
                    ws.close()
            except json.JSONDecodeError:
                self.error_occurred.emit("Invalid JSON received")

        def on_error(ws, error):
            """Called when error occurs."""
            self.error_occurred.emit(f"WebSocket error: {str(error)}")

        def on_close(ws, close_status_code, close_msg):
            """Called when connection closes."""
            pass

        # Create and connect WebSocket
        self._ws = websocket.WebSocketApp(
            SSO_URL,
            on_open=on_open,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
        )

        # Run in a separate thread
        self._thread = threading.Thread(target=self._ws.run_forever, daemon=True)
        self._thread.start()

    def disconnect(self):
        """Disconnect from SSO server."""
        if self._ws:
            self._ws.close()
