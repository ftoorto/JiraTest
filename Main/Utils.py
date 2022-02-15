import os
import subprocess
import time
import re


def _cmd_device(cmd:str, device:str):
    if device is not None:
        if device[-5:] != ":5555":
            device = device + ":5555"
        return cmd[:4] + ' -s %s ' % device + cmd[4:]
    else:
        return cmd


def _operate(cmd:str, device:str, time_to_sleep:int):
    actual_cmd = _cmd_device(cmd, device)
    proc = subprocess.Popen(actual_cmd, stdout=subprocess.PIPE, shell=True)
    time.sleep(time_to_sleep)
    return proc


def up(device=None):
    original_cmd = "adb shell input keyevent DPAD_UP"
    _operate(original_cmd, device, 1)


def down(device=None):
    original_cmd = "adb shell input keyevent DPAD_DOWN"
    _operate(original_cmd, device, 1)


def left(device=None):
    original_cmd = "adb shell input keyevent DPAD_LEFT"
    _operate(original_cmd, device, 1)


def right(device=None):
    original_cmd = "adb shell input keyevent DPAD_RIGHT"
    _operate(original_cmd, device, 1)


def ok(device=None,i=1):
    original_cmd = "adb shell input keyevent ENTER"
    _operate(original_cmd, device, i)


def back(device=None):
    original_cmd = "adb shell input keyevent BACK"
    _operate(original_cmd, device, 1)


def home(device=None):
    original_cmd = "adb shell input keyevent HOME"
    _operate(original_cmd, device, 1)


def fast_forward(device=None, time=1):
    original_cmd1 = "adb shell sendevent /dev/input/event6: 0004 0004 000c0045"
    original_cmd2 = "adb shell sendevent /dev/input/event6: 0001 006a 00000001"
    original_cmd3 = "adb shell sendevent /dev/input/event6: 0000 0000 00000000"
    original_cmd4 = "adb shell sendevent /dev/input/event6: 0004 0004 000c0045"
    original_cmd5 = "adb shell sendevent /dev/input/event6: 0001 006a 00000000"
    original_cmd6 = "adb shell sendevent /dev/input/event6: 0000 0000 00000000"

    _operate(original_cmd, device, time)


def rewind(device=None, time=1):
    original_cmd = "adb shell input keyevent KEYCODE_MEDIA_REWIND"
    _operate(original_cmd, device, time)


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


def __power(device=None, i=5):
    cmd = "adb shell input keyevent POWER"
    _operate(cmd, device, 1)
    time.sleep(i)


def __on_status():
    # TODO
    return "On"


def power_status():
    cmd = "adb shell dumpsys power |findstr mWakefulness"

    result = re.split(' |\n|\t|=|\r', os.popen("adb shell dumpsys power |findstr mWakefulness").read())[3]
    expect_result = {0: "Asleep", 1: "Awake"}
    # TODO


def power_on(device=None, i=5):
    cmd = "adb shell dumpsys power |findstr mWakefulness"
    proc = _operate(cmd, device, 0)
    result = re.split(' |\n|\t|=|\r', proc.stdout.read().decode())[3]
    if result == "Asleep":
        print("唤醒设备")
        __power(device,i)
    else:
        print("设备已是On模式，无需唤醒")


def power_off(device=None, i=5):
    cmd = "adb shell dumpsys power |findstr mWakefulness"
    proc = _operate(cmd, device, 0)
    result = re.split(' |\n|\t|=|\r', proc.stdout.read().decode())[3]
    if result != "Asleep":
        print("standby设备")
        __power(device,i)
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
