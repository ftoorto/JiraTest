import os
import time




def start_test():
    i = 0
    while (True):
        i = i + 1
        os.system("adb connect 192.168.1.102")
        os.system("adb devices")
        time.sleep(5)
        os.system("adb shell reboot")
        print(i, " times reboot")
        time.sleep(150)
        if(i>3000):
            break

if __name__ == "__main__":
    start_test()