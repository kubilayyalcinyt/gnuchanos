import io
import os, random
import PySimpleGUI as sg
from PIL import Image 



sg.LOOK_AND_FEEL_TABLE["gnuchan"] = {
                                    'BACKGROUND': '#240046',
                                    'TEXT': '#9d4edd',
                                    'INPUT': '#9d4edd',
                                    'TEXT_INPUT': '#240046',
                                    'SCROLL': '#3c096c',
                                    'BUTTON': ('#c77dff', '#5a189a'),
                                    'PROGRESS': ('#c77dff', '#5a189a'),
                                    'BORDER': 1, 'SLIDER_DEPTH': 0,'PROGRESS_DEPTH': 0, 
                                    }

themes = ['gnuchan', 'BlueMono', 'Black', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']

sg.theme("gnuchan")


file_types = [("JPEG (*.jpeg)", "*.jpeg"),
              ("JPG (*.jpg)", "*.jpg"),
              ("PNG (*.png)", "*.png"),
            ]



centerWindow = [
    [sg.Push()],
    [sg.Push(), sg.Image(key="-IMAGE-", size=(300, 300)), sg.Push()],
    [sg.Push()],
   
]


leftWindow = [
    [sg.Text("GnuChan Simple \n Image Viewer!", font="sans, 25")],
    [sg.Image("./logo.png")],
]
downWindow = [
    [sg.Text("Image File")],
    [sg.Input(size=(65, 1), key="-FILE-"), sg.FileBrowse(file_types=file_types, font="sans, 15" ), sg.Button("Load Image", font="sans, 15")],

    [sg.HSeparator()],

    [sg.Text("Click Fun Button", font="sans,35")],
    [sg.Button("Random Theme", font="sans, 15"), sg.VSeparator(), sg.Button("Exit", font="sans, 15")],
]


DefaultWindow = [
    [sg.Column(leftWindow), sg.VSeparator(), sg.Column(centerWindow)],
    [sg.HSeparator()],
    [sg.Column(downWindow)]
]


Window = sg.Window("GnuChan Simple Image Viewer!", DefaultWindow)






while True:  # Event Loop
    event, values = Window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == "Load Image":
        filename = values["-FILE-"]
        
        if os.path.exists(filename):
            image = Image.open(values["-FILE-"])
            image.thumbnail((400, 400))
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            Window["-IMAGE-"].update(data=bio.getvalue())    




    if event == "Random Theme":
            Window.close()
            sg.theme("random.choice(themes)")


            centerWindow = [
                [sg.Push()],
                [sg.Push(), sg.Image(key="-IMAGE-", size=(300, 300)), sg.Push()],
                [sg.Push()],
            
            ]


            leftWindow = [
                [sg.Text("GnuChan Simple \n Image Viewer!", font="sans, 25")],
                [sg.Image("./logo.png")],
            ]
            downWindow = [
                [sg.Text("Image File")],
                [sg.Input(size=(65, 1), key="-FILE-"), sg.FileBrowse(file_types=file_types, font="sans, 15" ), sg.Button("Load Image", font="sans, 15")],

                [sg.HSeparator()],

                [sg.Text("Click Fun Button", font="sans,35")],
                [sg.Button("Random Theme", font="sans, 15"), sg.VSeparator(), sg.Button("Exit", font="sans, 15")],
            ]


            DefaultWindow = [
                [sg.Column(leftWindow), sg.VSeparator(), sg.Column(centerWindow)],
                [sg.HSeparator()],
                [sg.Column(downWindow)]
            ]


            Window = sg.Window("GnuChan Music Download", DefaultWindow)