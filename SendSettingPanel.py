import tkinter as tk
import tkinter.ttk as ttk


class SendSettingPanel:

    def __init__(self):
        self.size = "400x560"

        self.root = tk.Tk()
        self.root.title("UDP send test")
        self.root.geometry(self.size)

        # 外部から設定用のコールバック
        self.on_client_change = lambda ip, port: print(ip, port)
        self.on_value_change = lambda value: print(value)

        # 送信先設定・表示用変数
        self.ip = tk.StringVar()
        self.ip.set("127.0.0.1")

        self.port = tk.StringVar()
        self.port.set("9999")

        self.current_client_text = tk.StringVar()

        # 値UI表示状態
        self.is_show_value = False

        # --- クライアント設定 ---
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, padx=8, pady=16, side='top')
        tk.Label(frame, text="Client Setting", font=("", 12, "bold")).pack(anchor=tk.W, padx=8, side='left')

        # IP入力
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, padx=8, pady=8, side='top')
        tk.Label(frame, text="IP", width=8).pack(fill=tk.Y, padx=8, side='left')
        tk.Entry(frame, textvariable=self.ip, width=15).pack(fill=tk.Y, padx=8, side='left')

        # Port入力
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, padx=8, pady=8, side='top')
        tk.Label(frame, text="Port", width=8).pack(fill=tk.Y, padx=8, side='left')
        tk.Entry(frame, textvariable=self.port, width=10).pack(fill=tk.Y, padx=8, side='left')

        # 現在設定表示
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, padx=8, pady=24, side='top')
        tk.Label(frame, textvariable=self.current_client_text).pack(padx=8, fill="x")

        # クライアント設定ボタン
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, padx=16, pady=8, side='top')
        tk.Button(frame, command=self._on_click_client_set, text='Set', width=100).pack(fill=tk.BOTH, padx=8, side='left')

        # セパレータ
        ttk.Separator(self.root).pack(fill=tk.BOTH, padx=8, pady=16, side='top')

    def show_value_form(self):
        if self.is_show_value:
            return

        self.is_show_value = True

        # 値設定・表示用変数
        self.key = tk.StringVar()
        self.key.set("NFL")
        self.key.trace_add("write", self._on_change_value)

        self.index = tk.StringVar()
        self.index.set("0")
        self.index.trace_add("write", self._on_change_value)

        self.value = tk.StringVar()
        self.value.set("50")
        self.value.trace_add("write", self._on_change_value)

        self.current_value_text = tk.StringVar()

        # --- 送信値設定 ---
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, padx=8, pady=8, side='top')
        tk.Label(frame, text="Value Setting", font="x 12 bold").pack(anchor=tk.W, padx=8, side='left')

        # Key値
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, padx=8, pady=8, side='top')
        tk.Label(frame, text="Key", width=8).pack(fill=tk.Y, padx=8, side='left')
        tk.Entry(frame, textvariable=self.key, width=5).pack(fill=tk.Y, padx=8, side='left')

        # Index値
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, padx=8, pady=8, side='top')
        tk.Label(frame, text="Index", width=8).pack(fill=tk.Y, padx=8, side='left')
        scale = tk.Scale(
            frame,
            variable=self.index,
            orient=tk.HORIZONTAL,
            from_=0.0,
            to=8.0,
            resolution=1.0,
            length=300
        )
        scale.pack(fill=tk.Y, padx=8, side='left')

        # Value値
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, padx=8, pady=8, side='top')
        tk.Label(frame, text="Value", width=8).pack(fill=tk.Y, padx=8, side='left')
        scale = tk.Scale(
            frame,
            variable=self.value,
            orient=tk.HORIZONTAL,
            from_=0.0,
            to=100.0,
            resolution=1.0,
            length=300
        )
        scale.pack(fill=tk.Y, padx=8, side='left')

        # 送信値
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, padx=8, pady=24, side='top')
        tk.Label(frame, textvariable=self.current_value_text).pack(padx=8, fill="x")

    def _on_click_client_set(self):
        self.current_client_text.set("Current client is " + self.ip.get() + ":" + self.port.get())
        self.show_value_form()
        self.on_client_change(self.ip.get(), int(self.port.get()))
        self._on_change_value()

    def _on_change_value(self, *args):
        if len(self.key.get()) != 3:
            return

        send_data = self.key.get() + "_" + self.index.get() + "_" + self.value.get()
        self.current_value_text.set("Sent data '" + send_data + "'")
        self.on_value_change(send_data)

    def move_window(self, x, y):
        self.root.geometry(self.size + "+" + str(x) + "+" + str(y))

    def update(self):
        self.root.update()


if __name__ == '__main__':

    ui = SettingUI()
    ui.move_window(200, 200)
    while True:
        ui.update()
