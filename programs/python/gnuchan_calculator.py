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


number1 = ""
number2 = ""
equal = ""

number1_F = True

pluspp = False
multiply = False
minus = False
divided = False

math_screen = [
    [
    sg.Text(number1, key="number1", font="sans, 20"),
    sg.Text("", key="math_Ass", font="sans, 20"),
    sg.Text(number2, key="number2", font="sans, 20"),
    sg.Text("", key="equal-str", font="sans, 20"),
    sg.Text(equal, key="equal", font="sans, 20"),
    ],
    
]

upWindow = [
    [sg.VPush(), sg.Text("Welcome GnuChan calculator", font="sans, 20"), sg.VPush()],
    [sg.VPush(), sg.Column(math_screen), sg.Push()]

]



leftWin = [
    [sg.Button("1", font="sans, 20"),sg.Button("2", font="sans, 20"),sg.Button("3", font="sans, 20"), sg.Button("GO", font="sans, 20", size=(3,1))],
    [sg.Button("4", font="sans, 20"),sg.Button("5", font="sans, 20"),sg.Button("6", font="sans, 20"), sg.Button("-", font="sans, 20", size=(3,1))],
    [sg.Button("7", font="sans, 20"),sg.Button("8", font="sans, 20"),sg.Button("9", font="sans, 20"), sg.Button("*", font="sans, 20", size=(3,1))],
    [sg.Button("0", font="sans, 20"),sg.Button("=", font="sans, 20"),sg.Button("/", font="sans, 20", size=(1,1)), sg.Button("+", font="sans, 20", size=(3,1))],
    [sg.Button("Clear", font="sans, 20")]
]

left2Win = [
    [sg.Image("./logo.png")]
]


downWindow = [
    [sg.Text("Click Fun Button", font="sans,35")],
    [sg.Button("Random Theme", font="sans, 15"), sg.VSeparator(), sg.Button("Exit", font="sans, 15")],
]

windowX_Adam = [
    [sg.Column(upWindow)],
    [sg.HSeparator()],
    [sg.Column(left2Win), sg.VSeparator(), sg.Column(leftWin), sg.VSeparator()],
    [sg.HSeparator()],
    [sg.Column(downWindow)]

]

Window = sg.Window("GnuChan Calculator", windowX_Adam)





while True:  # Event Loop
    event, values = Window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if number1_F == True:
        if event == "1":
            number1 += "1"
            Window["number1"].update(number1)
        elif event == "2":
            number1 += "2"
            Window["number1"].update(number1)
        elif event == "3":
            number1 += "3"
            Window["number1"].update(number1)
        elif event == "4":
            number1 += "4"
            Window["number1"].update(number1)
        elif event == "5":
            number1 += "5"
            Window["number1"].update(number1)
        elif event == "6":
            number1 += "6"
            Window["number1"].update(number1)
        elif event == "7":
            number1 += "7"
            Window["number1"].update(number1)
        elif event == "8":
            number1 += "8"
            Window["number1"].update(number1)
        elif event == "9":
            number1 += "9"
            Window["number1"].update(number1)
        elif event == "0":
            number1 += "0"
            Window["number1"].update(number1)
    elif number1_F == False:
        if event == "1":
            number2 += "1"
            Window["number2"].update(number2)
        elif event == "2":
            number2 += "2"
            Window["number2"].update(number2)
        elif event == "3":
            number2 += "3"
            Window["number2"].update(number2)
        elif event == "4":
            number2 += "4"
            Window["number2"].update(number2)
        elif event == "5":
            number2 += "5"
            Window["number2"].update(number2)
        elif event == "6":
            number2 += "6"
            Window["number2"].update(number2)
        elif event == "7":
            number2 += "7"
            Window["number2"].update(number2)
        elif event == "8":
            number2 += "8"
            Window["number2"].update(number2)
        elif event == "9":
            number2 += "9"
            Window["number2"].update(number2)
        elif event == "0":
            number2 += "0"
            Window["number2"].update(number2)

    if event == "+":
        number1_F = False
        pluspp = True
        Window["math_Ass"].update(" + ")
    if event == "*":
        number1_F = False
        multiply = True
        Window["math_Ass"].update(" * ")
    if event == "-":
        number1_F = False
        minus = True
        Window["math_Ass"].update(" - ")
    if event == "/":
        number1_F = False
        divided = True
        Window["math_Ass"].update(" / ")
    
    
    if event == "=":
        Window["equal-str"].update(" = ")
        if pluspp == True:
            equal = int(number1) + int(number2)
            Window["equal"].update(str(equal))
        elif multiply == True:
            equal = int(number1) * int(number2)
            Window["equal"].update(str(equal))
        elif minus == True:
            equal = int(number1) - int(number2)
            Window["equal"].update(str(equal))
        elif divided == True:
            equal = int(number1) / int(number2)
            Window["equal"].update(str(equal))


    if event == "Clear":
        number1_F = True
        pluspp = multiply = minus = divided = False

        number1 = ""
        number2 = ""

        Window["math_Ass"].update("")
        Window["equal"].update("")
        Window["number1"].update("")
        Window["number2"].update("")
        Window["equal-str"].update("")
    
    if event == "GO":
        number1 = str(equal)
        Window["number1"].update(str(number1))

        number1_F = True
        pluspp = multiply = minus = divided = False

        number2 = ""

        Window["math_Ass"].update("")
        Window["equal"].update("")
        Window["number2"].update("")
        Window["equal-str"].update("")
            

    if event == "Random Theme":
        sg.theme("random.choice(themes)")
        math_screen = [
            [
            sg.Text(number1, key="number1", font="sans, 20"),
            sg.Text("", key="math_Ass", font="sans, 20"),
            sg.Text(number2, key="number2", font="sans, 20"),
            sg.Text("", key="equal-str", font="sans, 20"),
            sg.Text(equal, key="equal", font="sans, 20"),
            ],
            
        ]

        upWindow = [
            [sg.VPush(), sg.Text("Welcome GnuChan calculator", font="sans, 20"), sg.VPush()],
            [sg.VPush(), sg.Column(math_screen), sg.Push()]

        ]



        leftWin = [
            [sg.Button("1", font="sans, 20"),sg.Button("2", font="sans, 20"),sg.Button("3", font="sans, 20"), sg.Button("GO", font="sans, 20", size=(3,1))],
            [sg.Button("4", font="sans, 20"),sg.Button("5", font="sans, 20"),sg.Button("6", font="sans, 20"), sg.Button("-", font="sans, 20", size=(3,1))],
            [sg.Button("7", font="sans, 20"),sg.Button("8", font="sans, 20"),sg.Button("9", font="sans, 20"), sg.Button("*", font="sans, 20", size=(3,1))],
            [sg.Button("0", font="sans, 20"),sg.Button("=", font="sans, 20"),sg.Button("/", font="sans, 20", size=(1,1)), sg.Button("+", font="sans, 20", size=(3,1))],
            [sg.Button("Clear", font="sans, 20")]
        ]

        left2Win = [
            [sg.Image("./logo.png")]
        ]


        downWindow = [
            [sg.Text("Click Fun Button", font="sans,35")],
            [sg.Button("Random Theme", font="sans, 15"), sg.VSeparator(), sg.Button("Exit", font="sans, 15")],
        ]

        windowX_Adam = [
            [sg.Column(upWindow)],
            [sg.HSeparator()],
            [sg.Column(left2Win), sg.VSeparator(), sg.Column(leftWin), sg.VSeparator()],
            [sg.HSeparator()],
            [sg.Column(downWindow)]

        ]

        Window = sg.Window("GnuChan Calculator", windowX_Adam)










Window.close()