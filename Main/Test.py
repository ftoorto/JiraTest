import subprocess
import time

import Utils as STB

def script():
    proc=subprocess.Popen("adb shell dumpsys power")
    proc.wait()
    print(proc.poll())


if __name__ == '__main__':
    script()