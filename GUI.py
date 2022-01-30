#!/usr/bin/env python
# coding: utf-8


import PySimpleGUI as sg
from opencv import *
import cv2

sg.theme("LightGreen")

# Define the window layout
video_layout = [
    [sg.Text("QueueMeet Demo", size=(20, 1), justification="center")],
    [sg.Image(filename="", key="-IMAGE-")]
]

lCol_layout = [
    [sg.Text("Bob", size=(10, 1), justification="left")],
    [sg.Image(filename="x.png", key="-Bob-", size=(209,209))],
    [sg.Text("Cole", size=(10, 1), justification="left")],
    [sg.Image(filename="x.png", key="-Cole-", size=(209,209))]
]

rCol_layout = [
    [sg.Text("Dylan", size=(10, 1), justification="left")],
    [sg.Image(filename="x.png", key="-Dylan-", size=(209,209))],
    [sg.Text("Evan", size=(10, 1), justification="left")],
    [sg.Image(filename="x.png", key="-Evan-", size=(209,209))]
]

layout = [[
    sg.Column(video_layout),
    sg.VSeperator(),
    sg.Column(lCol_layout),
    sg.Column(rCol_layout),
]]


window = sg.Window("QueueMeet", layout, location=(800, 400))
# Setup videocapture
cap = cv2.VideoCapture(0)

# Array of names to iterate through
names = ['Bob', 'Cole', 'Evan', 'Dylan']

while True:
    event, values = window.read(timeout=20)
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    # Get the frame from the opencv capture
    ret, frame = cap.read()
    
    # read the qr code and check against the 4 names
    qr = read_QRcodes(frame)[1]
    if(qr != 0):
        for j in names:
            if qr == j.lower():
                window["-" + j + "-"].update(filename='xray.png')
    else:
        for j in names:
            window["-" + j + "-"].update(filename='x.png')

    # Convert frame to a diplayable image
    imgbytes = cv2.imencode(".png", frame)[1].tobytes()
    
    # Display
    window["-IMAGE-"].update(data=imgbytes)
    
window.close()






