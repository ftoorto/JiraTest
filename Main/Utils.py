import os
import time
import re

def up(device=None):
    if device is None:
        os.popen("adb shell input keyevent DPAD_UP")
    else:
        os.popen("adb -s %s shell input keyevent DPAD_UP" % device)
    time.sleep(1)


def down(device=None):
    if device is None:
        os.popen("adb shell input keyevent DPAD_DOWN")
    else:
        os.popen("adb -s %s shell input keyevent DPAD_DOWN" % device)
    time.sleep(1)


def left(device=None):
    if device is None:
        os.popen("adb shell input keyevent DPAD_LEFT")
    else:
        os.popen("adb -s %s shell input keyevent DPAD_LEFT" % device)
    time.sleep(1)


def right(device=None):
    if device is None:
        os.popen("adb shell input keyevent DPAD_RIGHT")
    else:
        os.popen("adb -s %s shell input keyevent DPAD_RIGHT" % device)
    time.sleep(1)


def ok(device=None):
    if device is None:
        os.popen("adb shell input keyevent ENTER")
    else:
        os.popen("adb -s %s shell input keyevent ENTER" % device)
    time.sleep(1)


def back(device=None):
    if device is None:
        os.popen("adb shell input keyevent BACK")
    else:
        os.popen("adb -s %s shell input keyevent BACK"%device)
    time.sleep(1)


def home():
    os.system("adb shell input keyevent HOME")
    time.sleep(5)


def fast_forward(i=1):
    os.system("adb shell input keyevent KEYCODE_MEDIA_FAST_FORWARD")
    time.sleep(i)


def rewind(i=1):
    os.system("adb shell input keyevent KEYCODE_MEDIA_REWIND")
    time.sleep(i)


def play(device=None, i=1):
    if not device:
        os.system("adb shell input keyevent KEYCODE_MEDIA_PLAY")
    else:
        os.system("adb -s %s shell input keyevent KEYCODE_MEDIA_PLAY" % device)
    time.sleep(i)


def pause(device=None, i=1):
    if not device:
        os.system("adb shell input keyevent KEYCODE_MEDIA_PAUSE")
    else:
        os.system("adb -s %s shell input keyevent KEYCODE_MEDIA_PAUSE" % device)
    time.sleep(i)


def __power(i=5):
    os.system("adb shell input keyevent POWER")
    time.sleep(i)


def __on_status():
    # TODO
    return "On"


def power_status():
    result = re.split(' |\n|\t|=|\r', os.popen("adb shell dumpsys power |findstr mWakefulness").read())[3]
    expect_result = {0: "Asleep", 1: "Awake"}
    # TODO


def power_on(i=5):
    result = result = re.split(' |\n|\t|=|\r', os.popen("adb shell dumpsys power |findstr mWakefulness").read())[3]
    if result == "Asleep":
        print("唤醒设备")
        __power(i)
    else:
        print("设备已是On模式，无需唤醒")


def power_off(i=5):
    result = result = re.split(' |\n|\t|=|\r', os.popen("adb shell dumpsys power |findstr mWakefulness").read())[3]
    if result == "Awake":
        print("standby设备")
        __power(i)
    else:
        print("设备已是睡眠模式，无需再次睡眠")


def reboot(device=None, i=100):
    if not device:
        os.system("adb shell reboot")
    else:
        os.system("adb -s %s shell reboot" % device)
    time.sleep(i)


def settings(device=None):
    if device is None:
        os.popen("adb shell am start -n com.android.tv.settings/com.android.tv.settings.MainSettings")
    else:
        os.popen("adb -s %s shell am start -n com.android.tv.settings/com.android.tv.settings.MainSettings" % device)
    time.sleep(1)


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
