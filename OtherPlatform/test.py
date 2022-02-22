import subprocess
import sys
import time

import Main.Utils as STB


def start_test(device):
    proc = subprocess.Popen("adb -s %s shell dumpsys power" % device, stdout=subprocess.PIPE, bufsize=-1,
                            shell=True)

    for line in iter(proc.stdout.readline,''):
        print(line)
    proc.stdout.close()
    return


if __name__ == '__main__':
    dev = sys.argv[1]
    start_test(dev)
