import socket


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))
    print("Connected to server")
    data = client_socket.recv(1024)
    print("Received from server: {}".format(data.decode()))
    client_socket.close()


if __name__ == "__main__":
    start_client()
