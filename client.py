import socket
if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8080))
    client.send(bytes("I am CLIENT!","utf-8"))
    from_server = client.recv(4096)
    client.send(bytes("Closing now!","utf-8"))
    client.close()
    print(from_server.decode("utf-8"))