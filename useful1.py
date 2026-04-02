import time
import pyautogui

# 若需要安全退出，可在移动鼠标到屏幕左上角（默认）触发pyautogui.FailSafeException。
pyautogui.FAILSAFE = True

try:
    while True:
        pyautogui.click(button="right")
        time.sleep(1)
except KeyboardInterrupt:
    print("已停止（Ctrl+C）")