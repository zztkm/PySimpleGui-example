import json

import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import popup

from ssl_checker import SSLChecker

SSLChecker = SSLChecker()

# デザインテーマの設定
sg.theme("DarkAmber")

# windowに配置するコンポーネントの設定
layout = [
    [sg.Text("SSL対応かチェックしたいドメインを入力してくれ"), sg.InputText()],
    [sg.Button("チェック実行"), sg.Button("Cancel")]
]


# windowの生成
window = sg.Window("PySimpleGui example", layout)


# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    elif event == "チェック実行":
        host = values[0]
        args = {
            "hosts": [host]
        }
        cert = SSLChecker.get_cert(host, 443, SSLChecker.get_args(json_args=args))
        result = SSLChecker.get_cert_info(host, cert)
        print(result["host"])
        print(result["cert_valid"])
        popup_msg = "SSL対応している！" if result["cert_valid"] else "SSL対応していません。しっかりしてください！"
        sg.popup(f"Your Input: {popup_msg}")


window.Close()
