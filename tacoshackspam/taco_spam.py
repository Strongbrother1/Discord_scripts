import pyautogui, time
"""
Basic Program to spam discord "TacoShack" bot
"""
# Sleep to tab into program
time.sleep(5)
i,k = 0,1
# Infinite loop, do ctrl + c to quit in terminal
while i < k:
    pyautogui.typewrite("/work")
    time.sleep(1)
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.typewrite("/tips")
    time.sleep(1)
    pyautogui.press("enter")
    pyautogui.press("enter")
    # Sleep 5 minutes + 2 seconds to account for latency/lag
    time.sleep(5 * 60 + 2)
    pyautogui.typewrite("/tips")
    time.sleep(1)
    pyautogui.press("enter")
    pyautogui.press("enter")
    # Sleep 5 minutes + 2 seconds to account for latency/lag
    time.sleep(5 * 60 + 2)
