import socket
import pickle
from _thread import *
from threading import Thread

from QMserver import Datapackage


class QMpatient:
    DEFAULT_HOST = '127.0.0.1'
    DEFAULT_PORT = 2004

    def __init__(self, ID, host=DEFAULT_HOST, port=DEFAULT_PORT):
        self.ID = ID
        self.key = str()
        self.host = host
        self.port = port

    def connect(self):
        import PySimpleGUI as sg
        patient_socket = socket.socket()
        patient_socket.connect((self.host, self.port))
        self.key = patient_socket.recv(2048).decode('utf-8')
        disp_layout = [
            [sg.Image(filename="x.png", key=f"-{self.ID}-", size=(209, 209))]
        ]
        UI = sg.Window(f"Patient {self.ID}", [[sg.Column(disp_layout)]], location=(800, 400))
        while True:
            try:
                print('check0!!')
                event, _ = UI.read(timeout=5000)
                print('check1!!')
                # if event == "Exit" or event == sg.WIN_CLOSED:
                #     break
                print('check1!!')
                compressed_data = patient_socket.recv(2048)
                print('check2!!')
                extracted_file_name = self.attempt_open(compressed_data)
                if extracted_file_name:
                    print('Recognized!!')
                    UI["-" + str(self.ID) + "-"].update(filename="xray.png")
                else:
                    UI["-" + str(self.ID) + "-"].update(filename='x.png')
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


def startPatient(ID,key):
    patient = QMpatient(ID, key)
    patient.connect()


if __name__ == "__main__":
    patient = QMpatient(ID=3)
    # thread = Thread(target=startPatient, args=(patient,))
    patient.connect()
    # thread.start()
    # thread.join()
