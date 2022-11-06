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

    number1 = ""
    number2 = ""
    number1Type = True
    equal = int()
    math = ""
    math_symbol = ""
    mathLOG = ""
    line = 0



    rightWindow = [
        [sg.Push(), sg.Text("Gnuchan Calculator", font="san, 20", justification="c"), sg.Push()],
        [sg.Push(), sg.Text(math, key="mathSTR", font="sans, 20", justification="c", background_color="#130124", size=(15,1)), sg.Push()],

        [
            sg.Push(), 
            sg.Button("1", font="sans, 25"), sg.VSeparator(), sg.Button("2", font="sans, 25"), sg.VSeparator(), sg.Button("3", font="sans, 25"),
            sg.Push(),
        ],

        [
            sg.Push(), 
            sg.Button("4", font="sans, 25"), sg.VSeparator(), sg.Button("5", font="sans, 25"), sg.VSeparator(), sg.Button("6", font="sans, 25"),
            sg.Push(),
        ],

        [
            sg.Push(), 
            sg.Button("7", font="sans, 25"), sg.VSeparator(), sg.Button("8", font="sans, 25"), sg.VSeparator(), sg.Button("9", font="sans, 25"),
            sg.Push(),
        ],
        [sg.Push(), sg.VSeparator(), sg.Button("0", font="sans, 25"), sg.VSeparator()   , sg.Push()],

    ]

    rightWindowX = [
        [sg.Push(), sg.Text("This is MATH BRO", font="sans, 20"), sg.Push()],
        [
            sg.Push(),
            sg.Button("+", font="sans, 25"), sg.VSeparator(), 
            sg.Button("-", font="sans, 25"), sg.VSeparator(), 
            sg.Button("/", font="sans, 25"), sg.VSeparator(), 
            sg.Button("*", font="sans, 25"),
            sg.Push(),
        ],

        [sg.HSeparator()],

        [
            sg.Push(),
            sg.Button("=", font="sans, 25"), sg.VSeparator(),
            sg.Button("GO", font="sans, 25"), sg.VSeparator(), 
            sg.Button("Clean", font="sans, 25"),
            sg.Push(),
        ],
        [sg.Push(), sg.Multiline(font="sans, 20", key="mathLOG", disabled=True, justification="center", size=(20,4)), sg.Push()]

    ]

    downWindow = [
        [sg.Push(), sg.Text("uWu", font="sans, 20"), sg.Push()],
        [sg.Push(), sg.Button("GnuChan", font="sans, 15"), sg.Push()],
        [sg.VPush()],
        [sg.HSeparator()],
        [sg.Text("", size=(10,17))]

    ]

    mainWindow = [
        [sg.Column(downWindow), sg.VSeparator(), sg.Column(rightWindow), sg.VSeparator(), sg.Column(rightWindowX)],
    ]

    Window = sg.Window("GnuChan Default", mainWindow)

    while True:  # Event Loop
        event, values = Window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "GnuChan":
            gnuchanos()
        
        if event in ["1","2","3","4","5","6","7","8","8","9","0"]:
            if number1Type == True:
                number1 += event
            else:
                number2 += event
    

        if event in ["+","-","/","*"]:
            math_symbol = event
            number1Type = False


        if event == "=":
            if math_symbol == "+":
                equal = int(number1) + int(number2)
            elif math_symbol == "-":
                equal = int(number1) - int(number2)
            elif math_symbol == "*":
                equal = int(number1) * int(number2)
            elif math_symbol == "/":
                equal = int(number1) / int(number2)

            line += 1
            mathLOG += f"{line}: {number1} {math_symbol} {number2} = {equal} \n"
            Window["mathLOG"].update(mathLOG)

        if event == "Clean":
            number1 = ""
            number2 = ""
            number1Type = True
            math_symbol = ""
            equal = 0

            math = "Clear Finish"
            Window["mathSTR"].update(math)


        if event == "GO":
            number1Type = True
            number2 = ""
            math_symbol = ""
            number1 = str(int(equal))
            equal = 0


        if number1 == "":
            number1 = ""
            number2 = ""
            math_symbol = ""
            number1Type = True
        else:
            math = number1 + math_symbol + number2 + "=" + str(int(equal))
            Window["mathSTR"].update(math)

        print(number1 + math_symbol + number2)


if __name__ == "__main__":
    main()