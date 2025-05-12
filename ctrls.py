# 現在のウィンドウ名を取得
window_title = window.get_active_title()

# ウィンドウ名に "Chrome" が含まれている場合にのみ Ctrl+S を無効化
if "Chrome" in window_title:
    # Ctrl+S を無視する
    keyboard.send_keys('<ctrl>')
else:
    # Chrome以外では通常通り Ctrl+S を送信
    keyboard.send_keys('<ctrl>+s')