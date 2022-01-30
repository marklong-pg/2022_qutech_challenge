import PySimpleGUI as sg

sg.theme("LightGreen")

# Define the window layout
video_layout = [
    [sg.Text("QueueMeet Demo", size=(20, 1), justification="center")],
    [sg.Image(filename="", key="-IMAGE-")]
]

lCol_layout = [
    [sg.Text("Bob", size=(10, 1), justification="left")],
    [sg.Image(filename="x.png", key="-1-", size=(209,209))],
    [sg.Text("Cole", size=(10, 1), justification="left")],
    [sg.Image(filename="x.png", key="-2-", size=(209,209))]
]

provider_layout = [[sg.Column(video_layout)]]

window_default_provider = sg.Window("QueueMeet", provider_layout, location=(800, 400))
