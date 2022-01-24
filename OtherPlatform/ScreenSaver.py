import os
import time
from Main import Utils


def start_test():
    i = 1
    while True:
        i = i + 1
        os.system("adb connect 192.168.1.102")
        time.sleep(310)
        Utils.up()
        print(i, "times screen saver")
        if i > 50:
            break


if __name__ == "__main__":
    start_test()
