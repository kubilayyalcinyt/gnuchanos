import PySimpleGUI as sg
import os,random

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



second = 0
minute = 0
timerStart = False
strTime = ""


timer = [
    [sg.Text(key="time", font="sans, 20", background_color="#410f70", size=(30,1))],

    [
    sg.Button("Start", font="sans, 20"),
    sg.Button("Stop", font="sans, 20"), 
    sg.Button("Add Time", font="sans, 20"), 
    sg.Button("Exit", font="sans, 20")
    ],

    [sg.Image("./logo.png")],
    [sg.Text("Gnuchan Timer", font="sans, 20")]
]
timeNum = [
    [sg.Multiline(strTime, key="timenum", font="sans, 20", size=(20,10))]
]
downWindow = [
    [sg.Text("Click Fun Button", font="sans, 20")],
    [sg.Button("Random Theme", font="sans, 20")],
]
mainWindow = [
    [sg.Column(timer), sg.VSeparator(), sg.Column(timeNum)],
    [sg.HSeparator()],
    [sg.Column(downWindow)]
]

Window = sg.Window("Gnuchan Timer", mainWindow)


while True:  # Event Loop
    event, values = Window.read(timeout=60)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == "Start":
        timerStart = True
    if event == "Stop":
        timerStart = False
    if event == "Add Time":
        strTime += "Time: " + str(minute) + ":" + str(int(second)) + "\n" + "---------" + "\n"

        Window["timenum"].update(strTime)
    
    if timerStart == True:
        second += 0.05
        if second >= 60:
            minute += 1
            second = 0
        #print(second, " : ", minute)
        
                
        newtime = "Time: " + str(minute) + ":" + str(int(second))
        Window["time"].update(newtime)
    else:
        pass



    
    if event == "Random Theme":
        sg.theme("random.choice(themes)")
        timer = [
            [sg.Text(key="time", font="sans, 20", size=(30,1))],
            
            [
            sg.Button("Start", font="sans, 20"),
            sg.Button("Stop", font="sans, 20"), 
            sg.Button("Add Time", font="sans, 20"), 
            sg.Button("Exit", font="sans, 20")
            ],

            [sg.Image("./logo.png")],
            [sg.Text("Gnuchan Timer", font="sans, 20")]
        ]
        timeNum = [
            [sg.Multiline(strTime, key="timenum", font="sans, 20", size=(20,10))]
        ]
        downWindow = [
            [sg.Text("Click Fun Button", font="sans, 20")],
            [sg.Button("Random Theme", font="sans, 20")],
        ]
        mainWindow = [
            [sg.Column(timer), sg.VSeparator(), sg.Column(timeNum)],
            [sg.HSeparator()],
            [sg.Column(downWindow)]
        ]

        Window = sg.Window("Gnuchan Timer", mainWindow)