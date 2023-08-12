import socket, sys

args = sys.argv
if len(args) != 4:
    print("You need to enter arguments")
else:
    with socket.socket() as client_socket:
        host = str(args[1])
        port = int(args[2])

        client_socket.connect((host, port))
        message_to_send = args[3].encode()

        client_socket.send(message_to_send)

        response: bytes = client_socket.recv(1024)
        print(response.decode())
