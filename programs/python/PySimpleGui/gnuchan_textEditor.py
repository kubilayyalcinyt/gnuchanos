import PySimpleGUI as sg
from pathlib import Path


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

    fileSave = False

    downWindow = [
        [sg.Push(), sg.Text("uWu", font="sans, 20"), sg.Push()],
        [sg.Push(), sg.Button("GnuChan", font="sans, 15"), sg.Push()],
        
        [sg.HSeparator()],
        [sg.Text("", size=(10,40))]

    ]

    topWindow = [
        [
        sg.VSeparator(),
        sg.Button("Open File", font="sans, 20"), 
        sg.VSeparator(),
        sg.Button("Save", font="sans, 20"), 
        sg.VSeparator(),
        sg.Button("Save As", font="sans, 20"), 
        sg.VSeparator(),
        sg.Button("Help", font="sans, 20"), 
        sg.VSeparator(),
        ]
    ]

    RightWindow = [
        [sg.Push(), sg.Text("GnuChan Text Editor", font="sans, 20", size=(70,1), background_color="#130124", justification="center", expand_x=True), sg.Push()],
        [sg.HSeparator()],
        [sg.Text("File Name", font="sans, 20", justification="center", expand_x=True, key="fileName")],
        [sg.Multiline(font="sans, 15", key="multiTEXT", text_color="#9d4edd", expand_x=True, expand_y=True, size=(90,20), background_color="#380369")]
    ]

    mainWindow = [
        [sg.Column(downWindow), sg.VSeparator(), sg.Column(RightWindow), sg.VSeparator()],
        [sg.HSeparator()],
        [sg.Column(topWindow, background_color="#17022b", expand_x=True)],
    ]

    Window = sg.Window("GnuChan Text Editor", mainWindow, finalize=True)
  

    while True:  # Event Loop
        event, values = Window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "GnuChan":
            gnuchanos()


        if event == 'Open File':
            file_path = sg.popup_get_file('open',no_window = True)
            if file_path:
                file = Path(file_path)
                Window['multiTEXT'].update(file.read_text())
                Window['fileName'].update(file_path.split('/')[-1])
                fileSave = True

        if event == "Save As":
            file_path = sg.popup_get_file('SaveAs', no_window=True, save_as=True)
            if file_path:
                file = Path(file_path)
                file.write_text(values['multiTEXT'])
                Window['fileName'].update(file_path.split('/')[-1])
                fileSave = True
            

        if event == 'Save' and fileSave == True:
            file = Path(file_path)
            file.write_text(values['multiTEXT'])
            Window['fileName'].update(file_path.split('/')[-1])

        if event == "Help":
            pass

if __name__ == "__main__":
    main()