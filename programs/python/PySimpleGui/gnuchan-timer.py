import PySimpleGUI as sg


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
sg.theme("gnuchan")


def gnuchanos():
    MainWindow = [
        [
        sg.Push(), 
        sg.Text("GnuChanOS Ekstra", font="sans, 20", background_color="#0f001c"),
        sg.Push()
        ], 
        
        
        [sg.Image("./logo.png")], 
        ]

    window = sg.Window("GnuChanOS Programs HUB", MainWindow)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()




def main():

    second = 0
    minute = 0
    time = "Start Timer"
    timeStart = False
    timelog = ""
    rank = 0

    

    rightWindow = [
        [sg.Push(), sg.Text("GnuChanOS Basic Timer", font="sans, 20"), sg.Push()],
        [sg.Push(), sg.Text(time, key="timeSTR", font="sans, 20", background_color="#0f001c", size=(28,1), justification="c"), sg.Push()],

        [
        sg.Push(), 
        sg.Button("Start", font="sans, 20"), 
        sg.VSeparator(), 
        sg.Button("Stop", font="sans, 20"), 
        sg.VSeparator(), 
        sg.Button("Log", font="sans, 20"), 
        sg.VSeparator(),
        sg.Button("Clean", font="sans, 20"),
        sg.Push()
        ],


        [sg.Push(), sg.Multiline(timelog, font="sans, 20", key="addTimeLog", size=(28,10), disabled=True), sg.Push()]
    ]

    downWindow = [
        [sg.Push(), sg.Text("uWu", font="sans, 20"), sg.Push()],
        [sg.Push(), sg.Button("GnuChan", font="sans, 15"), sg.Push()],
        [sg.VPush()],
        [sg.HSeparator()],
        [sg.Text("", size=(10,26))]

    ]

    mainWindow = [
        [sg.Column(downWindow), sg.VSeparator(), sg.Column(rightWindow)],
    ]

    Window = sg.Window("GnuChan Timer", mainWindow)

    while True:  # Event Loop
        event, values = Window.read(timeout=60)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "GnuChan":
            gnuchanos()

        if event == "Start":
            timeStart = True
        if event == "Stop":
            timeStart = False
        if event == "Log":
            rank += 1
            timelog += f"{rank}: Minute: {minute} : Second: {int(second)} \n"
            Window["addTimeLog"].update(timelog)
        if event == "Clean":
            timeStart = False
            Window["addTimeLog"].update("")
            Window["timeSTR"].update("Start Timer")
            second = minute = 0

        
        if timeStart == True:
            time = "Minute: " + str(minute) + " : " + "Second: " + str(int(second))
            Window["timeSTR"].update(time)
            second += 0.05
        else:
            pass

        if second >= 60:
            minute += 1
            second = 0
        
        
        print(second)
        

if __name__ == "__main__":
    main()