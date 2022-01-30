import socket
import cv2
import PySimpleGUI as sg
from pyzbar import pyzbar
from GUI_setup import window_default_provider


class QMprovider:
    DEFAULT_HOST = '127.0.0.1'
    DEFAULT_PORT = 2004
    DEFAULT_UI = window_default_provider

    def __init__(self, UI=DEFAULT_UI, host=DEFAULT_HOST, port=DEFAULT_PORT):
        self.host = host
        self.port = port
        self.UI = UI

    @staticmethod
    def read_QRcodes(frame):
        file_name = str()
        QR_codes = pyzbar.decode(frame)
        for QR_code in QR_codes:
            x, y, w, h = QR_code.rect
            # decode QR code and put rectangle around the QR code
            file_name = QR_code.data.decode('utf-8')
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return frame, file_name

    def connect(self):
        provider_socket = socket.socket()
        try:
            provider_socket.connect((self.host, self.port))
        except socket.error as e:
            print(str(e))

        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        file_name_prev = str()
        while ret:
            event, _ = self.UI.read(timeout=20)
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            ret, frame = camera.read()
            frame, file_name_now = QMprovider.read_QRcodes(frame)
            img_bytes = cv2.imencode(".png", frame)[1].tobytes()
            self.UI["-IMAGE-"].update(data=img_bytes)

            if file_name_now != file_name_prev:
                try:
                    provider_socket.send(str.encode(file_name_now))
                    file_name_prev = file_name_now
                except (ConnectionResetError, ConnectionAbortedError):
                    print(f'Server disconnected!')
                    break
            if cv2.waitKey(1) & 0xFF == 27:
                break
        camera.release()
        self.UI.close()


if __name__ == "__main__":
    provider = QMprovider()
    provider.connect()
