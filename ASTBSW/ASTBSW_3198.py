import time

import Main.Utils as STB

def Hydra_home(device):
    STB._operate("adb shell am start -n com.tivo.hydra.app/.MainActivity", device, 5)

def Hydra_ok(device):
    STB._operate("adb shell input keyevent DPAD_CENTER",device,5)

def start_test(device):
    times=1
    while True:
        # STB.home(device)
        # time.sleep(5)
        # STB.back(device)
        # time.sleep(10)
        # STB.home(device)
        # STB._operate("adb shell am start https://www.youtube.com",device,20)
        # print("已循环%d次"%times)
        # times=times+1
        # if times>50:
        #     print("结束测试")
        #     return
        Hydra_home(device)
        time.sleep(5)
        STB.down(device)
        STB.right(device)
        time.sleep(5)
        Hydra_ok(device)
        time.sleep(10)
        times=times+1
        print("已循环%d次"%times)
        if times>100:
            print("测试结束")
            return

if __name__ == '__main__':
    start_test("192.168.1.105:5555")