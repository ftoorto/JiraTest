import os
import time




def start_test():
    i = 0
    while (True):
        i = i + 1

        os.system("adb connect 192.168.1.102")
        os.system("adb devices")
        
        time.sleep(5)

        for j in range(4):
            os.system("adb shell input keyevent DPAD_UP")
            time.sleep(1)
        for j in range(4):
            os.system("adb shell input keyevent DPAD_RIGHT")
            time.sleep(1)
        os.system("adb shell input keyevent ENTER ")
        time.sleep(1)
        for j in range(6):
            os.system("adb shell input keyevent DPAD_DOWN")
            time.sleep(1)
        os.system("adb shell input keyevent DPAD_UP")
        time.sleep(1)
        os.system("adb shell input keyevent ENTER ")
        time.sleep(1)
        for j in range(11):
            os.system("adb shell input keyevent DPAD_DOWN")
            time.sleep(1)
        os.system("adb shell input keyevent ENTER ")
        time.sleep(1)
        os.system("adb shell input keyevent ENTER ")
        time.sleep(1)
        for j in range(i%14):
            os.system("adb shell input keyevent DPAD_DOWN")
            time.sleep(1)
        os.system("adb shell input keyevent ENTER ")
        time.sleep(3)
        os.system("adb shell input keyevent DPAD_DOWN ")
        time.sleep(1)
        os.system("adb shell input keyevent ENTER ")
        time.sleep(1)
        os.system("adb shell input keyevent DPAD_RIGHT ")
        time.sleep(1)
        os.system("adb shell input keyevent ENTER ")
        time.sleep(1)

        print(i, " times reboot")
        time.sleep(100)
        if(i>3000):
            break

if __name__ == "__main__":
    start_test()