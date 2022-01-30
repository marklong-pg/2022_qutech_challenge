import socket
from _thread import *
# from QKDFunctions import wrap_data, Datapackage
from QKDFunctions import gen_key
import pickle

class QMserver:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket()
        self.provider_flag = True
        self.client_list = []
        self.key_dict = dict()
        self.patient_count = 0
        # TODO: prompt QKD and increase patient count instead

    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
        except socket.error as e:
            print(str(e))

        print('Socket is listening..')
        self.server_socket.listen(5)

    def send_to_patients(self, compressed_data):
        removal = []
        for client_socket, client_address in self.client_list:
            try:
                client_socket.sendall(compressed_data)
            except (ConnectionResetError, ConnectionAbortedError):
                print(f'Client @ {client_address} disconnected!')
                removal.append((client_socket, client_address))
                continue
        for client in removal:
            self.client_list.remove(client)

    def handle_provider(self, client_socket, client_address):
        while True:
            try:
                file_name = client_socket.recv(2048).decode('utf-8')
                target = int(file_name[0])
            except (ConnectionResetError, IndexError):
                print(f'Provider @ {client_address} disconnected!')
                break
            # implement wrapping and sending of compressed of data
            # REQUIRE: QRmessage format: "[Index of target recipient]_filename"
            #   e.g., string_data = "2_p000cX"

            data_package = wrap_data(file_name, target, self.key_dict)
            if not data_package: continue # TODO: prompt on provider screen file not found
            compressed_data = pickle.dumps(data_package)
            self.send_to_patients(compressed_data)
        client_socket.close()

    def accept_connections(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print('Connected to: ' + client_address[0] + ':' + str(client_address[1]))
            if self.provider_flag:
                print('Provider connected!')
                start_new_thread(self.handle_provider, (client_socket, client_address))
                self.provider_flag = False
            else:
                print('Patient connected! Generating key through QKD protocol BB84....')
                self.client_list.append((client_socket, client_address))
                self.patient_count = self.patient_count + 1
                key = ''.join(map(str, gen_key()))
                print(f'Generated key: {key}')
                self.key_dict[self.patient_count] = key
                client_socket.sendall(key.encode())
        self.server_socket.close()


def wrap_data(fname, target, key_dict):
    try:
        # Makes sure the file exists
        f = open(fname, 'r')
    except FileNotFoundError:
        # print('File does not exist.')
        return False
    # Makes sure the name is in the dict of keys
    if target in key_dict.keys():
        f.close()
        return Datapackage(fname, key_dict.get(target))
    else:
        return False


# Object to hold fname/file and associated key
class Datapackage():
    def __init__(self, fname, pword):
        self.fname = fname
        self.pword = pword

    def unlock(self, key):
        if (key == self.pword):
            return self.fname
        else:
            return False


if __name__ == "__main__":
    _host = '127.0.0.1'
    _port = 2004
    _key_dict = {1: 111, 2: 222, 3:333}
    server = QMserver(_host, _port)
    server.start()
    server.accept_connections()
