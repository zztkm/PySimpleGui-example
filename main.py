import PySimpleGUI as sg

# デザインテーマの設定
sg.theme("DarkAmber")

# windowに配置するコンポーネントの設定
layout = [
    [sg.Text("1行目")],
    [sg.Text("2行目: あつまれ俺の森!!!"), sg.InputText()],
    [sg.Button("OK"), sg.Button("Cancel")]
]


# windowの生成
window = sg.Window("PySimpleGui example", layout)


# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    elif event == "OK":
        print("Your Input: ", values[0])


window.Close()
