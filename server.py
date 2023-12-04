from flask import Flask, render_template
from flask_socketio import SocketIO
from socket_message_handler import MessageHandler

app = Flask(__name__)
socketio = SocketIO(app)
message_handler = MessageHandler(socketio)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("message")
def handle_message(message):
    message_type = message.get("type")
    print("message_type", message_type)
    handler_method = getattr(
        message_handler, f"handle_{message_type}", message_handler.handle_default
    )
    handler_method(message)


if __name__ == "__main__":
    socketio.run(app, debug=True)
