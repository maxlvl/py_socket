import socket

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    print("Listening on port " + str(port))
    connection, address = server_socket.accept()
    print("connection from: " + str(address))

    while True:
        data = connection.recv(1024).decode()
        if not data: 
            break
        print("from connected user: " + str(data))
        data = input(" -> ")
        connection.send(data.encode())

    connection.close()

if __name__ == "__main__":
    server_program()
