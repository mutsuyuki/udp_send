from UDPSender import UDPSender
from SendSettingPanel import SendSettingPanel


def main():
    sender = UDPSender()

    panel = SendSettingPanel()
    panel.move_window(40, 40)

    panel.on_client_change = lambda ip, port: sender.connect(ip, port)
    panel.on_value_change = lambda value: sender.send(value)

    while True:
        panel.update()


if __name__ == '__main__':
    main()
