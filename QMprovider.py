import socket
if __name__ == "__main__":

    ClientMultiSocket = socket.socket()
    host = '127.0.0.1'
    port = 2004

    try:
        ClientMultiSocket.connect((host, port))
    except socket.error as e:
        print(str(e))

    while True:
        Input = input('Message to send to patient: ')
        try:
            ClientMultiSocket.send(str.encode(Input))
        except (ConnectionResetError, ConnectionAbortedError):
            print(f'Server disconnected!')
            break
    ClientMultiSocket.close()