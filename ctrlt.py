# 現在のウィンドウ名を取得
window_title = window.get_active_class()

# ウィンドウ名に "xmind" が含まれている場合にのみ Ctrl+t を無効化
if "xmind" in window_title:
    # Ctrl+t を無視する
    keyboard.send_keys('<ctrl>')
else:
    # xmind以外では通常通り Ctrl+t を送信
    keyboard.send_keys('<ctrl>+t')
