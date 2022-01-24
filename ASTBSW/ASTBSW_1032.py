import sys

from Main import Utils as STB
import time


def start_test(device):
    i = 0
    if STB.adb_check(device):
        while True:
            i = i + 1
            STB.home()
            print("第", i, "Play YouTube")
            STB.ok()
            time.sleep(5)
            print("第", i, "Play live tv")
            STB.home()
            STB.down()
            STB.right()
            STB.ok()
            time.sleep(5)
            if i > 50:
                print("测试结束")
                break
    else:
        print("adb连接失败，检查连接")


if __name__ == "__main__":
    dev=sys.argv[1]
    start_test(dev)
