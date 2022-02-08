import subprocess


def _collect(device=None):
    if not device:
        subprocess.Popen("adb shell logcat -v time")


def _collect(findstr,device=None)
    if not device:
        subprocess.Popen("adb shell logcat -v time|findstr \'%s\'"%findstr)
    else:
        subprocess.Popen("adb -s %s shell logcat -v time|findstr \'%s\'"%(device,findstr))
