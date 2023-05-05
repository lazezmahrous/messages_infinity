import time
import pyautogui

# لوب ل تكرار الكود حسب عدد الرسائل التي تريدها
for i in range(10000):
    # لكتابه الرساله المراد ارسالها
    pyautogui.typewrite('i love you')
    time.sleep(0.0018)
    # لبعت الرساله المراد ارسالها
    pyautogui.press('enter')
