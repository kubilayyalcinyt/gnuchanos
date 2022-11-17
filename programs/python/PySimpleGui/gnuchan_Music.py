import PySimpleGUI as sg
import os


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

    filePath = "/home/gnuchanos/ or c:/"
    youtubeLink = "https://animegirl.youtube.com"
    filepathOkay = False
    downloadNow = ""

    FolderPathNotice = "Copy Your Folder Path Pleas"

    downWindow = [
        [sg.Push(), sg.Text("uWu", font="sans, 20"), sg.Push()],
        [sg.Push(), sg.Button("GnuChan", font="sans, 15"), sg.Push()],
        [sg.VPush()],
        [sg.HSeparator()],
        [sg.Text("", size=(10,26))]

    ]

    rightWindow = [
        [sg.Push(), sg.Text("GnuChan Music Download", font="sans, 20", justification="center"), sg.Push()],
        [sg.HSeparator()],
        
        [sg.Push(), sg.Input(filePath, font="sans, 20", key="folderPath"), sg.Button("Save Path", font="sans, 20"), sg.Push()],
        [sg.Push(), sg.Text(FolderPathNotice, font="sans, 20", justification="center", key="folderPathOkay"), sg.Push()],

        [sg.HSeparator()],

        [sg.Text("")], [sg.Text("Folder Path: ", key="finish", font="sans, 20", expand_x=True)], [sg.Text("")],

        [sg.HSeparator()],

        [sg.Push(), sg.Input(youtubeLink, font="sans, 20", key="ytLink"), sg.Button("Download", font="sans, 20"), sg.Push()],
        [sg.Push(), sg.Text("Youtube Link - Single video or playlist", font="sans, 20", justification="center"), sg.Push()],

        [sg.HSeparator()],

        [sg.Text("Tutorial: ctrl+C and Ctrl+V good luck \ndon't Forget This is just UI \npowerad by yt-dlp and PySimpleGUI", font="sans, 20")]

    ]

    mainWindow = [
        [sg.Column(downWindow), sg.VSeparator(), sg.Column(rightWindow)],
    ]

    Window = sg.Window("GnuChan Default", mainWindow)

    while True:  # Event Loop
        event, values = Window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "GnuChan":
            gnuchanos()



        if event == "Save Path":
            filePath = values["folderPath"]
            Window["finish"].update(f"Folder Path: {filePath}")
            filepathOkay = True



        if event == "Download":
            music_Link = values["ytLink"]
            if "https://www.youtube" in music_Link:
                downloadNow = False
                os.system(f"cd {filePath} && yt-dlp -f 'ba' -x --audio-format mp3 {music_Link}")
                downloadNow = True



        if downloadNow == True:
            Window["finish"].update(f"Folder Path: {filePath} | Music Download is Finish")
        elif downloadNow == False:
            Window["finish"].update(f"Folder Path: {filePath} | Music Download is start")



        if filepathOkay == True:
            FolderPathNotice = "You Can Download Now"
            Window["folderPathOkay"].update(FolderPathNotice)
        elif filepathOkay == False:
            FolderPathNotice = "Copy Your Folder Path Please"
            Window["folderPathOkay"].update(FolderPathNotice)


if __name__ == "__main__":
    main()