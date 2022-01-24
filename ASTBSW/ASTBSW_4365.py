import sys
import time

sys.path.append("../Main")
from Main import Utils as STB


def start_test(times=100):
    i = 0
    while True:
        STB.home()
        [STB.up() for i in range(4)]
        [STB.down() for i in range(2)]
        [STB.left() for i in range(4)]
        STB.right()
        STB.ok()
        time.sleep(20)
        STB.home()
        [STB.up() for i in range(4)]
        [STB.down() for i in range(2)]
        [STB.left() for i in range(4)]
        STB.right()
        STB.right()
        STB.ok()
        time.sleep(20)
        i = i + 1
        print("已测试%d次" % i)
        if i > times:
            return


if __name__ == '__main__':
    dev = sys.argv[1]
    start_test(dev)
