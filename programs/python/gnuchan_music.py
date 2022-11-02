import PySimpleGUI as sg
import os,random



music_Link = ""
defaultFilePath = "Empty"


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

leftWindow = [
    [sg.Text("Welcome To GnuChan Youtube Music Download GUI", font="sans,35")],
    [sg.Push(), sg.Image("./logo.png"), sg.Push()]
]

rightWindow = [
    [sg.Text("You Need Add Folder Path", font="sans, 20", key='-notice_me-')],
    [sg.Input(key="-download-"),sg.Button("Download")],
    [sg.Text(defaultFilePath, font="sans, 20", key="-FileFolder_Text-")],
    [sg.Input(key="-filepath-"),sg.Button("Save File Path")]

]

downWindow = [
    [sg.Text("Click Fun Button", font="sans,35")],
    [sg.Button("Random Theme", font="sans, 15"), sg.VSeparator(), sg.Button("Exit", font="sans, 15")],
]

defaulWindow = [
    [sg.Column(leftWindow), sg.VSeparator(), sg.Column(rightWindow)],
    [sg.HSeparator()],
    [sg.Column(downWindow)]
]

Window = sg.Window("GnuChan Music Download", defaulWindow)




while True:  # Event Loop
    event, values = Window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    if event == "Download":
        music_Link = values["-download-"]
        if "https://www.youtube" in music_Link:
            os.system(f"cd {defaultFilePath} && yt-dlp -f 'ba' -x --audio-format mp3 {music_Link}")
            Window["-notice_me-"].update("Your Download is Start Have a Nice Day :)")


    if event == "Save File Path":
        defaultFilePath = values["-filepath-"]
        Window["-notice_me-"].update("Download now")
        Window["-FileFolder_Text-"].update(defaultFilePath)


    if event == "Random Theme":
        sg.theme("random.choice(themes)")

        leftWindow = [
            [sg.Text("Welcome To GnuChan Youtube Music Download GUI", font="sans,35")],
            [sg.Push(), sg.Image("./logo.png"), sg.Push()]
        ]

        rightWindow = [
            [sg.Text("You Need Add Folder Path", font="sans, 20", key='-notice_me-')],
            [sg.Input(key="-download-"),sg.Button("Download")],
            [sg.Text(defaultFilePath, font="sans, 20", key="-FileFolder_Text-")],
            [sg.Input(key="-filepath-"),sg.Button("Save File Path")]

        ]

        downWindow = [
            [sg.Text("Click Fun Button", font="sans,35")],
            [sg.Button("Random Theme", font="sans, 15"), sg.VSeparator(), sg.Button("Exit", font="sans, 15")],
        ]

        defaulWindow = [
            [sg.Column(leftWindow), sg.VSeparator(), sg.Column(rightWindow)],
            [sg.HSeparator()],
            [sg.Column(downWindow)]
        ]

        Window = sg.Window("GnuChan Music Download", defaulWindow)


Window.close()

