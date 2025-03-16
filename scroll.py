# This program is an autoscroller
# Controls:
# Press 
# s to pause/unpause
# a to slow down
# d to speed up
# w to break


import pyautogui
import keyboard
import time

scrollAmount = -400  
scrollDelay = 1     
paused = True       
lastScroll = time.time()

try:
    print("~Starting Auto Scroll~")
    while True:
        if keyboard.is_pressed('s'):
            paused = not paused
            if paused:
                print("Paused")
            else:
                print("Resumed")
            time.sleep(0.2)

        elif keyboard.is_pressed('d'):
            scrollDelay = max(0.1, scrollDelay - 0.1)
            print(f"Speeding up: Delay is now {scrollDelay} seconds")
            time.sleep(0.2)

        elif keyboard.is_pressed('a'):
            scrollDelay += 0.1
            print(f"Slowing down: Delay is now {scrollDelay} seconds")
            time.sleep(0.2)

        elif keyboard.is_pressed('w'):
            print("Auto Scroll Stopped")
            break

        current_time = time.time()
        if not paused and current_time - lastScroll >= scrollDelay:
            pyautogui.scroll(scrollAmount)
            lastScroll = current_time

        time.sleep(0.01)

except KeyboardInterrupt:
    pass
