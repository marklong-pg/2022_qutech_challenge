import socket
import pickle
from _thread import *
from threading import Thread
from QMserver import Datapackage
from time import sleep

class QMpatient:
    DEFAULT_HOST = '127.0.0.1'
    DEFAULT_PORT = 2004

    def __init__(self, ID, key, host=DEFAULT_HOST, port=DEFAULT_PORT):
        self.ID = ID
        self.host = host
        self.port = port
        self.key = key

    # TODO: create function to apply refreshing of keys

    def connect(self):
        patient_socket = socket.socket()
        patient_socket.connect((self.host, self.port))
        while True:
            try:
                compressed_data = patient_socket.recv(2048)
                # TODO: remove this when done debugging
                extracted_data = self.attempt_open(compressed_data)
                if extracted_data:
                    print(f"Client {self.ID}")
                # TODO: use thread to branch out the show of image
            except ConnectionResetError:
                print(f'Server disconnected!')
                break
        patient_socket.close()

    def attempt_open(self, compressed_data):
        data_package = pickle.loads(compressed_data)
        filename = data_package.unlock(self.key)
        return filename


def generate_patients(keys_dict):
    return list(QMpatient(ID, key) for ID, key in keys_dict.items)


def startPatient(patient):
    patient.connect()


if __name__ == "__main__":
    patient_list = [
        QMpatient(ID=1, key=111),
        QMpatient(ID=2, key=222),
        QMpatient(ID=3, key=333)
    ]

    thread_list = []
    for patient in patient_list:
        thread = Thread(target=startPatient, args=(patient,))
        thread_list.append(thread)
        thread.start()
    for thread in thread_list:
        thread.join()



