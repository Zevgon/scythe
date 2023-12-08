import json
from backend.board.board import Board
from backend.player import Player
from backend.enums import Faction


class MessageHandler:
    def __init__(self, socket):
        self.socket = socket

    def handle_get_board(self, message):
        board = Board()
        board.populate_map_with_starting_tokens(
            [Player("Jeremy", Faction.ALBION), Player("Yale", Faction.NORDIC)]
        )
        print(board.serialize())
        response = {"type": "getBoard", "board": json.dumps(board.serialize())}
        # response = {"type": "getBoard", "board": "123"}
        self.socket.emit("message", response)

    def handle_default(self, message):
        # Default handler for unknown message types
        response = {"type": "error", "data": "Unknown message type"}
        self.socket.emit("message", response)
