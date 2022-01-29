
import cv2
from pyzbar import pyzbar

# read QR code and save the code in a file(QPcode_result.txt)
def read_QRcodes(frame):
    QRcodes = pyzbar.decode(frame)
    for QRcode in QRcodes:
        x, y, w, h = QRcode.rect
        # decode QR code and put rectangle around the QR code
        QRcode_info = QRcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        with open("QRcode_result.txt", mode='w') as file:
            file.write("Recognized QRcode:" + QRcode_info)
    return frame

# read the medical image with the QR coded name


# get data from camera
def main():

    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()

    while ret:
        ret, frame = camera.read()
        frame = read_QRcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
