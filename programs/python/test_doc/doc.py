from curses import window
import PySimpleGUI as sg


#########################################################################################################################

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
# custom theme

sg.theme("gnuchan")  # default theme

themes = ['BlueMono', 'Black', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']
# themes List
#########################################################################################################################


#########################################################################################################################
# main window layer
winLayer  = [
    [sg.Text("text")],
    [sg.Image("GnuChan Software/logo.png")],
    [sg.Button("Random Theme")],
    [sg.Input(key="-filepath-"),sg.Button("Save File Path")], # key="-filepath-"
    [sg.Text("start", key="-yazı-")]
    # sg.VSeparator() sg.HSeparator() | sg.Push sg.VPush()
]

# sg.Text("text", font="sans, 20"))
#-----------------------------------------------------
#element içerisinde belirli parametreler key="-w-"
# size(200x200)
# font="sans, 20"
# for text justification="c") c --> center


# multiline - read only = disabled=True
# multiline - text center = justification="center"







# layer system
leftWindow = [
    [sg.Text("left Window", font="sans,35")],
]

rightWindow = [
    [sg.Text("right Window", font="sans, 20", key='-notice_me-')],

]

downWindow = [
    [sg.Text("down Window", font="sans,35")],
]

defaulWindow = down_win = [
    [sg.Column(leftWindow), sg.Column(rightWindow)],
    [sg.Column(downWindow)],
    [sg.Column(winLayer)]
]


Window = sg.Window("GnuChan Music Download", defaulWindow)

#########################################################################################################################


while True:
    event, values = Window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':   
        break
        
    if event == "Save File Path":
        print(values["-filepath-"])   # ------> sg.Input(key="-filepath-")


        use_Gnu_linux_bro = values["-filepath-"]
        Window["-yazı-"].update(use_Gnu_linux_bro)
    
"""
    if event == "Download":
        music_Link = values["-download-"]
        if "https://www.youtube" in music_Link:
            os.system(f"cd {defaultFilePath} && yt-dlp -f 'ba' -x --audio-format mp3 {music_Link}")
            Window["-notice_me-"].update("Your Download is Start Have a Nice Day :)")
"""