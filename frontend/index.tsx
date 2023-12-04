import React, { useCallback, useEffect, useState } from 'react';
import { createRoot } from 'react-dom/client';
import io from 'socket.io-client';

const App = () => {
  const [messageType, setMessageType] = useState('');
  const [receivedMessage, setReceivedMessage] = useState('');

  useEffect(() => {
    // Connect to the WebSocket server
    const socket = io('http://127.0.0.1:5000');  // Replace with your Flask server URL

    // Event handler for receiving messages from the server
    socket.on('message', (msg) => {
      console.log(msg)
      setReceivedMessage(msg.board);
    });

    // Clean up the WebSocket connection on component unmount
    return () => {
      socket.disconnect();
    };
  }, []);

  // Function to send a message to the server
  const sendMessage = useCallback(() => {
    const socket = io('http://127.0.0.1:5000');  // Replace with your Flask server URL
    socket.emit('message', { type: messageType });
  }, [messageType]);

  return (
    <div>
    <h1>WebSocket Example</h1>
    <div>
      <label>Message:</label>
      <input type="text" value={messageType} onChange={(e) => setMessageType(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
    </div>
    <div>
      <p>Received Message: {receivedMessage}</p>
    </div>
  </div>
  );
};

const domNode = document.getElementById('root');
const root = createRoot(domNode!);
root.render(<App />);
