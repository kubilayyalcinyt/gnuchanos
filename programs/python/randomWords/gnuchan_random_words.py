import PySimpleGUI as sg
import list, random

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
    words = ""
    wordsChange = ""

    upWindow = [
        [sg.Push(), sg.Text(words, key="wordsWin", font="sans, 20", justification="c", expand_x=True, background_color="#000000"), sg.Push()]
    ]

    rightWindow = [
        [sg.Push(), sg.Text("click Fun Button Bro", font="sans, 20"), sg.Push()],
        [sg.Push(), sg.Button("Random Words", font="sans, 20"), sg.Push()],
        [sg.HSeparator()],
        [
        sg.Push(), 
        sg.Button("Numbers", font="sans, 20"), 
        sg.Button("Colors", font="sans, 20"), 
        sg.Button("Days and Month", font="sans, 20"), 
        sg.Push()
        ],
        [sg.Push(), sg.Button("Important Words", font="sans, 20"), sg.Push()],
        
        
    ]

    downWindow = [
        [sg.Push(), sg.Text("uWu", font="sans, 20"), sg.Push()],
        [sg.VPush(), sg.Button("GnuChan", font="sans, 15"), sg.VPush()],
        [sg.HSeparator()],

    ]

    mainWindow = [
        [sg.Column(upWindow)],
        [sg.HSeparator()],
        [sg.Column(downWindow), sg.VSeparator(), sg.Column(rightWindow, expand_x=True)],
    ]

    Window = sg.Window("GnuChan Default", mainWindow)

    while True:  # Event Loop
        event, values = Window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "GnuChan":
            gnuchanos()


        if event == "Numbers":
            wordsChange = "Numbers"
        elif event == "Important Words":
            wordsChange = "Important Words"
        elif event == "Colors":
            wordsChange = "Colors"
        elif event == "Days and Month":
            wordsChange = "Days and Month"



        if wordsChange == "Important Words":
            words = random.choice(list.DaylyWords)
            Window["wordsWin"].update(words)
        elif wordsChange == "Numbers":
            words = random.choice(list.numbers)
            Window["wordsWin"].update(words)
        elif wordsChange == "Colors":
            words = random.choice(list.colors)
            Window["wordsWin"].update(words)
        elif wordsChange == "Days and Month":
            words = random.choice(list.days)
            Window["wordsWin"].update(words)           

if __name__ == "__main__":
    main()