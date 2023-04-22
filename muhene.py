# これはキーコード的にはAが入力されるはずだが何故かspaceが入る。
# 他のキーでもおかしいので一旦却下
#keyboard.send_keys("<code99>")
#keyboard.send_keys("<code103>")

# 一度ひらがなにしてから半角／全角キー入力
keyboard.send_keys("<code99>")
keyboard.send_keys("<code49>")


#keyboard.send_keys("<f13>")

# TODO: 動かないのでなんとかする。あとxdotool遅くてNG
# time.sleep(.2)
# system.exec_command("xdotool key Zenkaku")
# time.sleep(.2)
# system.exec_command("xdotool key Hankaku")