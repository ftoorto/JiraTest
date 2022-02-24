import subprocess
import sys
import time

import Main.Utils as STB


def start_test(device):
    proc = subprocess.Popen("adb -s %s shell dumpsys power" % device, stdout=subprocess.PIPE,
                            shell=True)
    proc.wait()
    for line in iter(proc.stdout.readline, 'b'):

        print(line)
    proc.stdout.close()
    return


if __name__ == '__main__':
    # dev = sys.argv[1]
    dev="192.168.144.53"
    start_test(dev)
