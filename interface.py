import PySimpleGUI as sg
import time

class RankingWindow:
    def __init__(self, data):
        rankings = sorted(data, key=lambda x: x[1], reverse=True)
        ranking_text = [sg.Text(f"{i}:", font=("Helvetica", 25), justification='right', size=(2,1), text_color="dark grey") for i in range(1, 11)]
        name_text = [sg.Text(f"   {name:15}", font=("Helvetica", 35), justification='center', size=(15,1), text_color="") for name, _ in rankings[:10]]
        points_text = [sg.Text(f"{number:3}", font=("Helvetica", 36), justification='left', size=(3,1),text_color="") for _, number in rankings[:10]]
        ranking_layout = [[ranking_text[i], name_text[i], points_text[i]] for i in range(len(name_text))]

        self.layout = [
            [sg.Text("TODAYS RANKING:", font=("Helvetica", 40), justification='center', size=(50,1), text_color="purple")],
            [sg.Column(ranking_layout[:9])],
            [sg.Button("New Game", button_color=('white', 'green'), size=(15, 1), font=("Helvetica", 14))],
        ]

        self.window = sg.Window("SHOOTING GAME", self.layout, resizable=True, size=(800, 600), element_justification="c").finalize()
        self.window.Maximize()

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                self.window.close()
                return 1
            elif event == "New Game":
                self.window.close()


class NewGameWindow:
    def __init__(self):

        self.game_layout = [
            [sg.Text("Enter your name:", font=("Helvetica", 50))],
            [sg.Multiline(key="name", pad=(0,(100,0)), size=(100,1), focus=True, font=("Helvetica", 120), no_scrollbar="true")],
            [sg.Button("Start Game", button_color=('white', 'green'), size=(40, 3), pad=(0,(60,0)), font=("Helvetica", 14), bind_return_key=True)]
        ]

        self.window = sg.Window("New Game", self.game_layout, resizable=True, element_justification="c").finalize()
        self.window.Maximize()

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                self.window.close()
                break
            elif event == "Start Game":
                name = values["name"]
                self.window.close()
                return name

        self.window.close()

class CountdownWindow:
    def __init__(self):
        self.layout = [[sg.Text(key="time", font=("Arial", 400), pad=(35,0,0,0))]]

        self.window = sg.Window("Countdown", self.layout, resizable=True, element_justification="c").finalize()
        self.window.Maximize()


    def run(self, game_time=20):

        time_remaining = game_time

        while True:
            event, values = self.window.read(timeout=1000)
            time_remaining -= 1
            if time_remaining == 3:
                self.window['time'].update(text_color="red", font=("Arial", 450))
            self.window['time'].update(time_remaining)

            if event == sg.WIN_CLOSED:
                self.window.close()
                break
            if time_remaining == 0:
                self.window.close()
                break