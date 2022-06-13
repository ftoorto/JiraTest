import sys
import time

sys.path.append("../Main")
from Main import Utils as STB


def start_test(times=10000):
    j = 0
    while True:
        STB.home()
        [STB.up() for i in range(4)]
        [STB.down() for i in range(1)]
        [STB.left() for i in range(4)]
        [STB.right() for i in range(2)]
        STB.ok()
        time.sleep(20)
        STB.home()
        [STB.up() for i in range(4)]
        [STB.down() for i in range(1)]
        [STB.left() for i in range(4)]
        [STB.right() for i in range(3)]
        STB.ok()
        time.sleep(20)
        STB.home()
        [STB.up() for i in range(4)]
        [STB.down() for i in range(1)]
        [STB.left() for i in range(4)]
        [STB.right() for i in range(4)]
        STB.ok()
        time.sleep(20)
        j = j + 1
        print("已测试%d次" % j)
        if j > times:
            return


def start_test_4045tlu(device):
    i = 0
    while True:
        # Netflix
        STB.home(device)
        time.sleep(5)
        [STB.up(device) for i in range(4)]
        [STB.down(device) for i in range(2)]
        [STB.left(device) for i in range(4)]
        STB.right(device)
        STB.ok(device)
        time.sleep(20)
        # Prime video
        STB.home(device)
        time.sleep(5)
        [STB.up(device) for i in range(4)]
        [STB.down(device) for i in range(2)]
        [STB.left(device) for i in range(4)]
        STB.right(device)
        STB.right(device)
        STB.ok(device)
        time.sleep(20)

        # YouTube
        STB.home(device)
        time.sleep(5)
        [STB.up(device) for i in range(4)]
        [STB.down(device) for i in range(2)]
        [STB.left(device) for i in range(4)]
        [STB.right(device) for i in range(3)]
        STB.ok(device)
        time.sleep(20)
        i = i + 1
        print("已测试%d次" % i)
        if i > 100000:
            return


if __name__ == '__main__':
    start_test()
