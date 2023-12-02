import websocket
import ssl

def send_and_receive_message(url, message):
    # Create a WebSocket connection
    ws = websocket.create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE})

    try:
        # Send a message
        ws.send(message)
        print("Sent:", message)

        # Receive a response
        response = ws.recv()
        print("Received:", response)
    finally:
        # Always close the connection
        ws.close()

if __name__ == "__main__":
    # URL of the WebSocket server (replace with your server's URL)
    server_url = "wss://3911-2601-8c-487e-b430-7506-72d5-9601-5495.ngrok-free.app/audiostream"

    # Message to send
    message_to_send = "Hello, server!"

    send_and_receive_message(server_url, message_to_send)
