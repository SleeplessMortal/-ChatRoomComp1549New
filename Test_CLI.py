import socket
import threading
import pickle
import sys
import pyautogui
import signal

def run_fake_server(self):
    # Run a server to listen for a connection and then close it
    server_sock = socket.socket()
    server_sock.bind(('192.168.0.8', 8000))
    server_sock.listen(0)
    server_sock.accept()
    server_sock.close()

def test_client_connects_and_disconnects_to_default_server(self):
    # Start fake server in background thread
    server_thread = threading.Thread(target=self.run_fake_server)
    server_thread.start()

    # Test the clients basic connection and disconnection
    client = Client.Client()
    client.connect('192.168.0.8', 8000)
    client.disconnect()

    # Ensure server thread ends
    server_thread.join()

def main():
    if len(sys.argv) < 3:
        print("Test Server is running")
        return
    listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listenSocket.bind((sys.argv[1], int(sys.argv[2])))
    listenSocket.listen(10)
    print("Server running")
    while True:
        client, _ = listenSocket.accept()
        threading.Thread(target=handshake, args=(client,)).start()

if __name__ == "__main__":
	main()