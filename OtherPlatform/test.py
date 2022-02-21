import subprocess
import sys
import time

import Main.Utils as STB


def start_test(device):
    proc = subprocess.Popen("adb -s %s logcat -v time|findstr error" % device, stdout=subprocess.PIPE, bufsize=-1,
                            shell=True)

    for line in iter(proc.stdout.readline, b''):
        print(line)
    proc.stdout.close()


if __name__ == '__main__':
    device = sys.argv[1]
    start_test(device)
