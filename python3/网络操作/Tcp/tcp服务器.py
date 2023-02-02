import socket


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(5)
    print("TCP server is listening on 0.0.0.0:12345")
    while True:
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from {}".format(client_address))
        client_socket.sendall(b"Hello, client!")
        client_socket.close()


if __name__ == "__main__":
    start_server()
