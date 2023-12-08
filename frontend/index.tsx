import React, {
  ReactEventHandler,
  useCallback,
  useEffect,
  useState,
} from "react";
import { createRoot } from "react-dom/client";
import io, { Socket } from "socket.io-client";

const App = () => {
  const [messageType, setMessageType] = useState("");
  const [receivedMessage, setReceivedMessage] = useState("");

  useEffect(() => {
    const socket = io("http://127.0.0.1:5000");
    socket.on("message", (msg) => {
      console.log(msg);
      setReceivedMessage(msg.board);
    });

    return () => {
      socket.disconnect();
    };
  }, []);

  const sendMessage: ReactEventHandler<HTMLButtonElement> = useCallback(
    (e) => {
      e.preventDefault();
      const socket = io("http://127.0.0.1:5000");
      socket.emit("message", { type: messageType });
    },
    [messageType]
  );

  return (
    <div>
      <h1>WebSocket Example</h1>
      <div>
        <label>Message:</label>
        <form>
          <input
            type="text"
            value={messageType}
            onChange={(e) => setMessageType(e.target.value)}
          />
          <button onClick={sendMessage}>Send</button>
        </form>
      </div>
      <div>
        <p>Received Message: {receivedMessage}</p>
      </div>
    </div>
  );
};

const domNode = document.getElementById("root");
const root = createRoot(domNode!);
root.render(<App />);
