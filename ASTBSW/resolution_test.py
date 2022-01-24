"""
    本代码已在Windows系统下测试可用，但不完美，在Linux环境下可能需要增加sudo以提升权限
"""
import sys
import time
import os


def adb_check(device, result_flag=True, auto_reconnect_flag=True):
    result = os.popen("adb devices", 'r')
    adb_devices = result.read()
    device_offline = device + "\toffline"
    if (adb_devices.find(device) != -1) and (adb_devices.find(device_offline) == -1):
        if result_flag:
            print("adb连接成功")
        return True
    else:
        if auto_reconnect_flag:
            cmd = "adb connect " + device
            os.system(cmd)
            time.sleep(3)
            if (adb_devices.find(device) != -1) and (adb_devices.find(device_offline) == -1):
                if result_flag:
                    print("adb重连成功")
                return True
            else:
                if result_flag:
                    print("result: adb连接断开")
                return False
        else:
            if result_flag:
                print("result: adb连接断开")
            return False


def settings(device=None):
    if device is None:
        os.popen("adb shell am start -n com.android.tv.settings/com.android.tv.settings.MainSettings")
    else:
        os.popen("adb -s %s shell am start -n com.android.tv.settings/com.android.tv.settings.MainSettings" % device)
    time.sleep(1)


def ok(device=None):
    if device is None:
        os.popen("adb shell input keyevent ENTER")
    else:
        os.popen("adb -s %s shell input keyevent ENTER" % device)
    time.sleep(1)


def down(device=None):
    if device is None:
        os.popen("adb shell input keyevent DPAD_DOWN")
    else:
        os.popen("adb -s %s shell input keyevent DPAD_DOWN" % device)
    time.sleep(1)


def right(device=None):
    if device is None:
        os.popen("adb shell input keyevent DPAD_RIGHT")
    else:
        os.popen("adb -s %s shell input keyevent DPAD_RIGHT" % device)
    time.sleep(1)


def up(device=None):
    if device is None:
        os.popen("adb shell input keyevent DPAD_UP")
    else:
        os.popen("adb -s %s shell input keyevent DPAD_UP" % device)
    time.sleep(1)


def start_test(device):
    try:
        times = 0
        while True:
            times = times + 1
            print("循环第%d次" % times)
            for j in range(15):
                if adb_check(device):
                    # 打开settings
                    settings(device)
                    time.sleep(3)
                    # 进入settings菜单
                    for i in range(5):
                        down(device)
                    up(device)
                    ok(device)
                    # 进入display菜单
                    for i in range(11):
                        down(device)
                    ok(device)
                    # 选择resolution
                    ok(device)
                    l = j % 15
                    if l == 0:
                        ok(device)
                    else:
                        for k in range(l):
                            down(device)
                            # 选定
                        ok(device)
                    # keep
                    down(device)
                    ok(device)
                    # 准备重启
                    right(device)
                    ok(device)
                    print("第", j + 1, "次重启")
                    time.sleep(90)
                else:
                    print("adb连接断开，测试失败")
                    return
            # 循环10次
            if times > 10:
                return
    except KeyboardInterrupt:
        print("测试中断")


if __name__ == "__main__":
    # 设备需要带上端口号
    # 如在命令行中声明设备，则使用以下代码
    # dev = sys.argv[1]

    # 设备ip和端口号
    dev = "192.168.1.104:5555"
    start_test(dev)
