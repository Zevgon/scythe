class MessageHandler:
    def __init__(self, socket):
        self.socket = socket

    def handle_get_board(self, data):
        response = {"type": "getBoard", "board": "123"}
        self.socket.emit("message", response)

    def handle_default(self, data):
        # Default handler for unknown message types
        response = {"type": "error", "data": "Unknown message type"}
        self.socket.emit("message", response)
