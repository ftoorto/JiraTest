import time

import Main.Utils as STB


def start_test(device):
    times=1
    while True:
        STB.home(device)
        time.sleep(5)
        STB.back(device)
        time.sleep(10)
        STB.home(device)
        STB._operate("adb shell am start https://www.youtube.com",device,20)
        print("已循环%d次"%times)
        times=times+1
        if times>50:
            print("结束测试")
            return

if __name__ == '__main__':
    start_test("192.168.1.109")